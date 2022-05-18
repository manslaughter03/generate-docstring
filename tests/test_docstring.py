"""

docstring test
"""
import os
from glob import glob

import pytest
import libcst as cst

from docstring.transformer import generate_typing_str 
from docstring.visitor import Visitor
from docstring import parse


def generate_parametrize() -> list:
    """

    generate_parametrize function

    Returns:
        list: list of tuple of parametrize pytest

    """
    parametrizes = []
    parametrize = ()
    for item in sorted(glob(os.path.join(os.path.dirname(__file__), 'testdata', "*.py"))):
        with open(item) as _file:
            if item.endswith("_expected.py"):
                parametrize += (_file.read(),)
            else:
                parametrize = (_file.read(),)
        if item.endswith("_expected.py"):
            parametrizes.append(pytest.param(*parametrize, id=os.path.basename(item)))
    return parametrizes


@pytest.mark.parametrize('code, expected', generate_parametrize())
def test_docstring_generate(code: str, expected: str):
    """

    test_docstring_generate function

    Args:
        code (str): code to parse
        expected (str): expected output

    """
    _original_node, _updated_node = parse(code, 'Username')
    assert _original_node != _updated_node
    assert _updated_node.code == expected


@pytest.mark.parametrize("statement, expected", [
    (
        "data: Dict[str, str]",
        "Dict[str, str]",
    ),
    (
        "data: typing.Dict[str, str]",
        "typing.Dict[str, str]",
    ),
    (
        "data: typing.Dict[typing.Dict[str, int], str]",
        "typing.Dict[typing.Dict[str, int], str]",
    ),
    (
        "data: typing.Tuple[str, str]",
        "typing.Tuple[str, str]"
    ),
    (
        "data: typing.Tuple[typing.Dict[str, str], str]",
        "typing.Tuple[typing.Dict[str, str], str]"
    ),
    (
        "data: typing.Tuple[str, ...]",
        "typing.Tuple[str, ...]"
    )
])
def test_recursive_typing(statement, expected):
    tree = cst.parse_statement(statement)
    annotation = tree.body[0].annotation
    typing_str = generate_typing_str(annotation)
    assert typing_str == expected
