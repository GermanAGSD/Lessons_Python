# main.py
from RxBus import RxBus

bus = RxBus()

def setup_receivers():
    bus.observe("user.created").subscribe(lambda x: print("✅ got:", x))
    bus.observe_latest("status").subscribe(lambda x: print("📌 status:", x))

def send():
    bus.publish_latest("status", "BOOTING")
    bus.publish("user.created", {"id": 1})
    bus.publish_latest("status", "READY")

if __name__ == "__main__":
    setup_receivers()
    send()
    input("Press Enter to exit...")
