from typing import Any, Union
from ..covers import *
from .Overrider import *


__all__ = [
    "FunctionLocker",
    "TypeLocker",
    "lock",
    "unlock"
]

BIF = type(input)
BIT = type


class __Locker:
    placeholder: Any
    __real = {}

    def __init__(self, placeholder: Any):
        self.placeholder = placeholder

    def lock(self, name: str):
        self.__real[name] = Overrider.override(name, self.placeholder)

    def unlock(self, name: str):
        if name not in self.__real:
            return
        Overrider.write(name, self.__real[name])
        del self.__real[name]


FunctionLocker = __Locker(LockedFunction)
TypeLocker = __Locker(LockedType)


def lock(obj: Union[BIF, type]):
    if isinstance(obj, BIF):
        FunctionLocker.lock(obj.__name__)

    elif isinstance(obj, type):
        if obj.__name__ not in __builtins__:
            raise ValueError("given obj is not in module builtins")
        TypeLocker.lock(obj.__name__)

    else:
        raise ValueError("Only support lock BIF or type")


def unlock(name: str):
    FunctionLocker.unlock(name)
    TypeLocker.unlock(name)
