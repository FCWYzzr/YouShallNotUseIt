__all__ = [
    "YouShallNotUseIt",
    "LockedType",
    "BannedType",
    "LockedFunction",
    "BannedFunction",
    "Lang", "lang"
]

from .Exceptions import YouShallNotUseIt
from .Types import LockedType, BannedType
from .Functions import LockedFunction, BannedFunction
from .Lang import Lang, lang


def applyDoc(self) -> None:
    pass
    LockedFunction.__doc__ = self.func.lockDoc
    BannedFunction.__doc__ = self.func.banDoc

    LockedType.__doc__ = self.type.lockDoc
    BannedType.__doc__ = self.type.banDoc


Lang.applyDoc = applyDoc

lang.applyDoc()
