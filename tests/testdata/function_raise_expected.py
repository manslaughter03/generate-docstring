"""
Username module
"""
from typing import List


class ForbiddenValue(Exception):
    """

    ForbiddenValue class

    """
    pass


def generate(args: List[str]) -> str:
    """

    generate function

    Args:
        args (List[str]): TODO: to complete

    Raises:
      ForbiddenValue: TODO: to complete

    Returns:
        str: TODO: to complete

    """
    _data = ""
    for item in args:
        if item == "inexist":
            raise ForbiddenValue("Forbidden value")
        _data += f", {item}"
    return _data
