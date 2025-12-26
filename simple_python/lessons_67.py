from typing import Union, Optional, Any, Final, Callable
import json

from OOP.lessons_oop_10 import person

# Аннотации типов


lst: list[int, str, bool] = [1, 2, 3, "3", True]
print(lst)

adder: tuple[int, str] = (1, 2, "dsdas")

book = tuple[str, str, int]
book = ('Baklagin', 'Annotation', 2022)

book2: tuple[str, str, int] = ('Pushkin', 'Annotation', 2023)

print(book)
print(book2)

# Сколько значений бы небыло будет тип float везде
elems: tuple[float, ...]
elems = (1.0,)
elems = (1.0, 2.0)
print(elems[1])

words: dict[str, int] = {'one': 1}
print(words)

persons: set[str] = {'sassa', 'sasa'}
print(persons)


def get_positive(digits: Optional[list[Union[int, float]]] = None) -> list[Union[int, float]]:
    if digits:
        return list(filter(lambda x: x > 0, digits))
    return []


print(get_positive([1, 2, 3, 5, 63]))


def get_digits(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    if lst is None:
        return []
    return list(filter(flt, lst))


def even(x: int):
    return bool(x % 2 == 0)


print(get_digits(even, [1, 2, 3, 4, 5, 6, 7]))
