from typing import Any

__all__ = [
    "Overrider"
]


class Overrider:
    BI: Any = __builtins__

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
