import asyncio
import aiohttp
import time

# URL вашего API
URL = "http://192.168.1.100:8001/gethosts"

# Количество одновременных подключений для теста
NUM_CONNECTIONS = 500

async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Response status: {response.status}, Data: {data[:100]}...")
            return data
    except Exception as e:
        print(f"Error fetching data: {e}")

async def run_load_test(url, num_connections):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for _ in range(num_connections)]

        # Запуск всех задач параллельно и замер времени выполнения
        start_time = time.time()
        await asyncio.gather(*tasks)
        end_time = time.time()

        print(f"All requests completed in {end_time - start_time:.2f} seconds")

# Запуск теста с использованием asyncio
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_load_test(URL, NUM_CONNECTIONS))
