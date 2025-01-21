from rx.subject import Subject

# Создание Subject (контроллер потока)
stream = Subject()

# # Подписка на поток
# stream.subscribe(lambda x: print(f"Subscriber 1 received: {x}"))
# stream.subscribe(lambda x: print(f"Subscriber 2 received: {x}"))

# Добавление данных в поток
# stream.on_next(10)
# stream.on_next(20)

# Завершение потока
# stream.on_completed()

