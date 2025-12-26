# singleton.py
class DataBus:
    """Простой Singleton для хранения общих данных"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # инициализация полей один раз
            cls._instance.data = {}
        return cls._instance

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)
