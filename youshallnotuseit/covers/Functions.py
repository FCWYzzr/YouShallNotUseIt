from typing import NoReturn, Any
from .Exceptions import YouShallNotUseIt
from .Lang import lang


def LockedFunction(*args, **kwargs) -> NoReturn:
    raise YouShallNotUseIt(lang.func.locked)


def BannedFunction(*args, **kwargs) -> NoReturn:
    raise YouShallNotUseIt(lang.func.banned)
