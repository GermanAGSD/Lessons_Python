# rx_bus.py
from collections import defaultdict
from rx.subject import Subject, BehaviorSubject

class RxBus:
    """Singleton-шина событий с именованными каналами."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Инициализация один раз
            cls._instance._subjects = defaultdict(Subject)          # обычные каналы
            cls._instance._behaviors = {}                           # каналы с последним значением
        return cls._instance

    # -------- обычные каналы (как StreamController.broadcast в Dart) --------
    def publish(self, channel: str, value):
        self._subjects[channel].on_next(value)

    def observe(self, channel: str):
        """Возврат Observable для Rx-операторов и подписки."""
        return self._subjects[channel]

    # -------- Behavior-каналы (поздние подписчики получают последнее значение) --------
    def publish_latest(self, channel: str, value):
        if channel not in self._behaviors:
            self._behaviors[channel] = BehaviorSubject(value)
        else:
            self._behaviors[channel].on_next(value)

    def observe_latest(self, channel: str):
        if channel not in self._behaviors:
            # Создаём пустой BehaviorSubject без стартового значения? В Rx это не ок.
            # Поэтому дадим None как первый снимок.
            self._behaviors[channel] = BehaviorSubject(None)
        return self._behaviors[channel]
