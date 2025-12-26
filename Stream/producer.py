# producer.py
import time
import random
from RxBus import RxBus

def main():
    bus = RxBus()

    i = 0
    while True:
        i += 1
        payload = {"n": i, "value": random.randint(1, 100)}
        bus.publish("numbers", payload)              # обычный канал
        bus.publish_latest("config.debug", i % 2 == 0)  # behavior-канал (последнее значение)

        print("[producer] sent ->", payload)
        time.sleep(0.4)

if __name__ == "__main__":
    main()
