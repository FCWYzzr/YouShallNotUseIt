from typing import Any
from sys import _getframe

__all__ = [
    "Overrider"
]


class Overrider:
    BI: Any

    @staticmethod
    def read(name: str) -> Any:
        """
        platform implementation defined
        """
        pass

    @staticmethod
    def write(name: str, value: Any) -> None:
        """
        platform implementation defined
        """
        pass

    @staticmethod
    def override(name: str, value: Any) -> Any:
        origin = Overrider.read(name)
        Overrider.write(name, value)
        return origin


import_frame_cost = 0
f = _getframe()
while True:
    import_frame_cost += 1
    f = f.f_back
    if f.f_locals.get("__file__", "").endswith(".py"):
        break


Overrider.BI = _getframe(import_frame_cost * 3).f_locals["__builtins__"]

if isinstance(Overrider.BI, dict):
    def __read(name):
        return Overrider.BI[name]

    def __write(name, value):
        Overrider.BI[name] = value

else:
    def __read(name):
        return Overrider.BI.__getattribute__(name)


    def __write(name, value):
        Overrider.BI.__setattr__(name, value)


Overrider.read = __read
Overrider.write = __write
