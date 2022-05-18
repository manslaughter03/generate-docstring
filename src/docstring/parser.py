"""

parser module
"""
from typing import Tuple

import libcst as cst
from jinja2 import Environment, PackageLoader, select_autoescape

from docstring.transformer import DocstringTransformer, Templates
from docstring.visitor import Visitor


def parse(code: str, module_name: str) -> Tuple[cst.Module, cst.Module]:
    """

    parse function

    Args:
        code (str): TODO: to complete
        module_name (str): TODO: to complete
        override (bool): TODO: to complete

    Returns:
        str: TODO: to complete

    """
    tree = cst.parse_module(code)
    env = Environment(
        loader=PackageLoader("docstring", "templates"), autoescape=select_autoescape()
    )
    templates: Templates = {
        cst.FunctionDef: env.get_template("function_def.py.jinja2"),
        cst.ClassDef: env.get_template("class_def.py.jinja2"),
        cst.Module: env.get_template("module.py.jinja2"),
    }
    visitor = Visitor()
    tree.visit(visitor)
    transformer = DocstringTransformer(
        templates, visitor.indents_func, visitor.indents_class, visitor.raises, module_name
    )
    modified_tree = tree.visit(transformer)
    return tree, modified_tree
