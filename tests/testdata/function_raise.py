from typing import List


class ForbiddenValue(Exception):
    pass


def generate(args: List[str]) -> str:
    _data = ""
    for item in args:
        if item == "inexist":
            raise ForbiddenValue("Forbidden value")
        _data += f", {item}"
    return _data
