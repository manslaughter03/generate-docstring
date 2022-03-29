"""

docstring test
"""
import os
import pytest
from docstring import parse


def generate_parametrize() -> list:
    """

    generate_parametrize function

    Returns:
        list: list of tuple of parametrize pytest

    """
    parametrizes = []
    for item in ['simple_function', 'class', 'class_init']:
        parametrize = ()
        for ext in ['.py', '_expected.py']:
            with open(os.path.join(os.path.dirname(__file__), 'testdata', f'{item}{ext}'), 'r') as _file:
                parametrize += (_file.read(),)
        parametrizes.append(parametrize)
    return parametrizes


@pytest.mark.parametrize('code, expected', generate_parametrize())
def test_docstring_generate(code: str, expected: str):
    """

    test_docstring_generate function

    Args:
        code (str): code to parse
        expected (str): expected output

    """
    assert parse(code, 'Username', True) + '\n' == expected
