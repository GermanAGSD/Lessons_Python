from typing import Union, Optional, Any, Final
# Union объеденение

# Аннотации типов
cnt: float = 0


def mul2(x: float, y: int = 2) -> float:
    return x * y

# Подмена через Alias
Digit = Union[int, float]
def mul3(x: Digit, y: Union[int, float] = 2) -> Union[int, float]:
    return x * y

# Optional только один тип и None
Str = Optional[str] # равносильно Union[str, None]
def mul4(x: float, y: Optional[int] = None) -> float:
    if y:
        print(f"{x}")
    return x * y


def mul2(x: Any, y: int = 2) -> float:
    return x * y



res = mul2(5)
print(res)
print(mul2.__annotations__)

res2 = mul3(5,4)
print(res2)
print(mul3.__annotations__)

res3 = mul4(5,4)
print(res3)
print(mul4.__annotations__)

x: dict[str, str] = {'car': 'car', 'color': 'color'}
print(x)