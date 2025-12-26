from typing import Union, Optional, Any, Final, Callable, Type, TypeVar
import json
# from __future__ import annotations
# Аннотации типов
cmd: str = "top"
# cmd = "top"

match cmd:
    case "top" | "buttom":
        print("top")
    case "left":
        print("left")
    case "right":
        print("right")
    case other:
        print("Over")

print("check end")