from typing import Union
from .Overrider import Overrider
from ..covers import *

__all__ = [
    "ban"
]

BIF = type(input)


def ban(obj: Union["BIF", type]):
    if isinstance(obj, BIF):
        Overrider.write(obj.__name__, BannedFunction)

    elif isinstance(obj, type):
        if obj.__name__ not in __builtins__:
            raise ValueError("given obj is not in module builtins")
        Overrider.write(obj.__name__, BannedType)

    else:
        raise ValueError("Only support ban BIF or type")
