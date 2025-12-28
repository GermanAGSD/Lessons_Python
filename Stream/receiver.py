# receiver.py
from RxBus import RxBus

bus = RxBus()

def on_user_created(data):
    print("✅ user.created:", data)

def on_status(value):
    print("📌 status(latest):", value)

# обычный канал: получишь только будущие события
sub1 = bus.observe("user.created").subscribe(on_user_created)

# latest-канал: при подписке сразу придёт последнее значение (или None)
sub2 = bus.observe_latest("status").subscribe(on_status)

if __name__ == "__main__":
    print("receiver started, waiting...")
    input()  # держим процесс живым
    sub1.dispose()
    sub2.dispose()
