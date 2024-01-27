from typing import Any
from .Lang import lang


class YouShallNotUseIt(Exception):
    
    def __init__(self, msg=None, *args):
        if msg is None:
            msg = lang.deny.default
        super().__init__(msg, *args)
