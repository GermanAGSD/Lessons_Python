import asyncio


async def func():
    """Выполнить трудоемкую задачу"""
    return 'str'



async def cor1():
    print('cor 1 start')
    for i in range(5):
        await asyncio.sleep(1.5)
        print('cor1', i)
    return 'str'

async def cor2():
    print('cor 2 start')
    for i in range(5):
        await asyncio.sleep(2)
        print('cor2', i)
    return 'str'

async def main():
    # Преобразование корутин в задачи
    task1 = asyncio.create_task(cor1())
    task2 = asyncio.create_task(cor2())
    task3 = asyncio.create_task(func())

    # Ожидание завершения задач
    await asyncio.wait([task1, task2, task3])
    # Получение результатов
    result1 = task1.result()
    result2 = task2.result()
    result3 = task3.result()

    print(f"Результат task1: {result1}")
    print(f"Результат task2: {result2}")
    print(f"Результат task3: {result3}")
# Запуск основного цикла
asyncio.run(main())

# res = asyncio.run(func())
# res2 = asyncio.run(cor1())
# res3 = asyncio.run(cor2())
#
# print(res)
# print(res2)
# print(res3)
# if __name__ == '__main__':
#     # Явное создание новой петли событий
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     result = loop.run_until_complete(func())
#     print(result)
#     loop.close()
