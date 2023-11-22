from dataclasses import dataclass


@dataclass
class Lang:
    @dataclass
    class LangPack:
        locked: str
        lockDoc: str
        banned: str
        banDoc: str

    deny: str
    func: LangPack
    type: LangPack

    def applyDoc(self) -> None:
        """
        see __init__.py
        """
        pass


lang = Lang(
    "You Shall Not Use This",
    Lang.LangPack(
        "This Function is Locked",
        "This Function is Locked",
        "This Function is Banned",
        "This Function is Banned"
    ),
    Lang.LangPack(
        "This Type is Locked",
        "This Type is Locked",
        "This Type is Banned",
        "This Type is Banned"
    )
)
