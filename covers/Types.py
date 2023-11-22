from .Exceptions import YouShallNotUseIt
from .Lang import lang


class LockedType:
    def __init__(self, *args, **kwargs):
        raise YouShallNotUseIt(lang.type.locked)


class BannedType:
    def __init__(self, *args, **kwargs):
        raise YouShallNotUseIt(lang.type.banned)
