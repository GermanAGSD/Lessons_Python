from typing import Union, Optional, Any, Final, Callable, Type, TypeVar
import json

from mypy.util import json_dumps

req = {'server': '127.0.0.1', 'login': 'root', 'password': '1234', 'port': 24}
# result = connect_d(req)
