from typing import Union, Optional, Any, Final, Callable, Type, TypeVar
import json

from mypy.util import json_dumps

req = {
    'url': 'https://devprog777.ru',
    'method': 'GET',
    'timeout': 1000,
}

match req:
    case {'url': url, 'method': method, 'timeout': timeout} if len(req) >= 3:
        print(f"Запрос url {url}, method {method}, timeout {timeout}")
    case _:
        print("неверный запрос")

a = json_dumps(req)
print(a)