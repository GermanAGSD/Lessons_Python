# consumer.py
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler
from RxBus import RxBus

def main():
    bus = RxBus()

    # Пример 1: Реактивный пайплайн над каналом "numbers"
    sub1 = (
        bus.observe("numbers")
        .pipe(
            ops.map(lambda d: d["value"]),  # берём поле
            ops.filter(lambda v: v % 2 == 0),
            ops.buffer_with_count(5),       # батчим по 5 элементов
        )
        .subscribe(lambda batch: print("[consumer] even batch:", batch))
    )

    # Пример 2: Канал с последним состоянием (BehaviorSubject)
    # Поздний подписчик мгновенно получит текущее значение.
    sub2 = (
        bus.observe_latest("config.debug")
        .pipe(
            ops.distinct_until_changed()
        )
        .subscribe(lambda v: print("[consumer] debug mode =", v))
    )

    # (необязательно) пример планировщика, если идёт многопоточность:
    # pool = ThreadPoolScheduler(2)
    # sub3 = bus.observe("numbers").pipe(ops.observe_on(pool)).subscribe(...)

    try:
        print("consumer running. Press Ctrl+C to exit.")
        import threading; threading.Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        sub1.dispose()
        sub2.dispose()

if __name__ == "__main__":
    main()
