"""

parser module
"""
import ast
from jinja2 import Environment, PackageLoader, select_autoescape
from docstring.transformer import DocStringTransformer, Templates


def parse(code: str, module_name: str, override: bool = False) -> str:
    """

    parse function

    Args:
        code (str): code to parse and update
        module_name (str): module name
        override (bool): override existing docstring

    Returns:
        str: code updated

    """
    env = Environment(
        loader=PackageLoader("docstring", "templates"), autoescape=select_autoescape()
    )
    templates: Templates = {
        ast.FunctionDef: env.get_template("function_def.py.jinja2"),
        ast.ClassDef: env.get_template("class_def.py.jinja2"),
        ast.Module: env.get_template("module.py.jinja2"),
    }
    visitor = DocStringTransformer(templates, module_name, override)
    tree = ast.parse(code)
    visitor.visit(tree)
    return ast.unparse(tree)
