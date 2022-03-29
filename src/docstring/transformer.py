"""

DocStringTransformer
"""
import ast
from typing import Union, Any, Dict
from jinja2 import Template

Statement = Union[ast.Module, ast.ClassDef, ast.FunctionDef]
Templates = Dict[Any, Template]


class DocStringTransformer(ast.NodeTransformer):
    """

    DocStringTransformer class

    Args:
        templates (Templates): list of templates
        module_name (str): module name
        override (bool): override docstring existing

    """

    def __init__(self, templates: Templates, module_name: str, override: bool = False):
        """

        DocStringTransformer function

        Args:
        templates (Templates): list of templates
        module_name (str): module name
        override (bool): override docstring existing

        """
        ast.NodeTransformer.__init__(self)
        self._templates = templates
        self._module_name = module_name
        self._override = override

    def _append_expr(self, node: Statement, res: str):
        """

        _append_expr function, add docstring in ast.Statement with res
        of templating.

        Args:
            node (Statement): node to update
            res (str): docstring data

        """
        _exprs = [
            item
            for item in node.body
            if isinstance(item, ast.Expr) and isinstance(item.value, ast.Constant)
        ]
        if not _exprs:
            node.body.insert(0, ast.Expr(ast.Constant(res)))
        elif self._override:
            node.body[0] = ast.Expr(ast.Constant(res))

    def visit_Module(self, node: ast.Module):
        """

        visit_Module function, Module callback

        Args:
            node (ast.Module): current module

        """
        super().generic_visit(node)
        _args = {"name": self._module_name}
        _res = self._templates[ast.Module].render(_args)
        self._append_expr(node, _res)
        super().generic_visit(node)
        return node

    def visit_ClassDef(self, node: ast.ClassDef):
        """

        visit_ClassDef function, ClassDef callback

        Args:
            node (ast.ClassDef): current class definition

        """
        _init_args = next(
            filter(
                lambda x: isinstance(x, ast.FunctionDef) and x.name == "__init__",
                node.body,
            ),
            None,
        )
        _args = {
            "name": node.name,
            "attributes": [
                item for item in node.body if isinstance(item, ast.AnnAssign)
            ],
            "_indent": node.col_offset,
            "args": [item for item in _init_args.args.args if item.arg not in "self"]
            if _init_args
            else [],
        }
        _res = self._templates[ast.ClassDef].render(_args)
        self._append_expr(node, _res)
        super().generic_visit(node)
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """

        visit_FunctionDef function, FunctionDef callback

        Args:
            node (ast.FunctionDef): current function definition

        """
        _args = {
            "name": node.name,
            "args": [item for item in node.args.args if item.arg not in "self"],
            "return_type": node.returns.id
            if isinstance(node.returns, ast.Name)
            else None,
            "_indent": node.col_offset,
        }
        _res = self._templates[ast.FunctionDef].render(_args)
        self._append_expr(node, _res)
        super().generic_visit(node)
        return node
