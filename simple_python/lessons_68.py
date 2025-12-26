from typing import Union, Optional, Any, Final, Callable, Type, TypeVar
import json
# from __future__ import annotations
# Аннотации типов

tr: dict = {'car': 'машина'}
x: object = None
x = '123'
x = 123
print(x)


class Geom: pass


class Line(Geom): pass


def factory_object(cls_object: Type[Geom]) -> Geom:
    return cls_object()

T = TypeVar("T", bound=Geom)
geom: Geom = factory_object(Geom)
point: Line = factory_object(Line)
g: Geom
g = Line()

a: Any = None
s: str
s = a
print(s)

class Point2d:
    x: int
    y: int

    def __init__(self, x: int , y: int) -> None:
        self.x = x
        self.y = y

    def getter(self) -> Union[str, ...]:
        return self.x, self.y

    def copy(self) -> 'Point2d':
        return Point2d(self.x, self.y)

p = Point2d(10,20)
p.x = 10
print(p.copy())
print(p.getter())
