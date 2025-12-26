from typing import Union, Optional, Any, Final, Callable, Type, TypeVar
import json

cmd = ("Baklagin", "python", 2000.78)

match cmd:
    case tuple() as book:
        print(f"кортеж: {book}")
    case _:
        print("непонятный формат")

match cmd:
    case author, title, price:
        print(f"кортеж: {author}, {title}, {price}")
    case _:
        print("непонятный формат")