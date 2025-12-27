# consumer.py
import time
from RxBus import RxBus

def main():
    bus = RxBus()

    # Подписка на обычный канал
    sub_numbers = bus.observe("numbers").subscribe(
        on_next=lambda payload: print("[consumer] numbers <-", payload),
        on_error=lambda e: print("[consumer] numbers error:", e),
        on_completed=lambda: print("[consumer] numbers completed"),
    )

    # Подписка на behavior-канал (получит последнее значение сразу; если ещё не было — придёт None)
    sub_debug = bus.observe_latest("config.debug").subscribe(
        on_next=lambda v: print("[consumer] config.debug <-", v),
        on_error=lambda e: print("[consumer] config.debug error:", e),
        on_completed=lambda: print("[consumer] config.debug completed"),
    )

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[consumer] stopping...")
        sub_numbers.dispose()
        sub_debug.dispose()

if __name__ == "__main__":
    main()
