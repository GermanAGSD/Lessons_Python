import socket

server_ip = "127.0.0.1"
server_port = 15000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

message = "Hello, server!"
sock.sendall(message.encode())

response = sock.recv(1024)
print("Ответ от сервера:", response.decode())

sock.close()
