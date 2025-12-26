import asyncio

async def handle_client(reader, writer):
    try:
        request_line = await reader.readline()
        if not request_line:
            writer.close()
            await writer.wait_closed()
            return

        headers = {}
        while True:
            line = await reader.readline()
            if line in (b'\r\n', b'\n', b''):
                break
            line_str = line.decode(errors='ignore')
            if ':' in line_str:
                key, value = line_str.split(':', 1)
                headers[key.strip()] = value.strip()

        target_host, target_port = request_line.decode().split()[1].split(":")
        proxy_addr = headers.get("X-Proxy-Address")

        if proxy_addr:
            try:
                proxy_host, proxy_port = proxy_addr.split(":")
                remote_reader, remote_writer = await asyncio.open_connection(proxy_host, int(proxy_port))
                remote_writer.write(f"CONNECT {target_host}:{target_port} HTTP/1.1\r\nHost: {target_host}:{target_port}\r\n\r\n".encode())
                await remote_writer.drain()

                # Пропускаем заголовки ответа от прокси
                while True:
                    line = await remote_reader.readline()
                    if not line or line in (b'\r\n', b'\n'):
                        break

                print(f"[+] Forwarding through proxy: {proxy_host}:{proxy_port}")
            except Exception as e:
                print(f"[!] Failed to connect to proxy {proxy_addr}: {e}")
                writer.close()
                await writer.wait_closed()
                return
        else:
            print(f"[+] Direct connect: {target_host}:{target_port}")
            remote_reader, remote_writer = await asyncio.open_connection(target_host, int(target_port))

        # Ответ клиенту
        try:
            writer.write(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            await writer.drain()
        except Exception as e:
            print(f"[!] Failed to write 200 OK to client: {e}")
            writer.close()
            await writer.wait_closed()
            remote_writer.close()
            await remote_writer.wait_closed()
            return

        async def pipe(reader, writer):
            try:
                while True:
                    data = await reader.read(4096)
                    if not data:
                        break
                    writer.write(data)
                    await writer.drain()
            except Exception:
                pass
            finally:
                try:
                    writer.close()
                    await writer.wait_closed()
                except:
                    pass

        await asyncio.gather(
            pipe(reader, remote_writer),
            pipe(remote_reader, writer)
        )

    except Exception as e:
        print(f"[!] Error in connection handler: {e}")
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except:
            pass

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 8080)
    print("[+] Async proxy server listening on port 8080")
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Server stopped by user.")
