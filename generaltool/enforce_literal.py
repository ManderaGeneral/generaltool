from sys import _getframe
from typing import Literal, get_args, get_origin

def _obj_is_from_typing(obj):
    return type(obj).__name__.startswith("typing.")

def _check_value_to_literal(kwargs, name, literal):
    value = kwargs[name]
    args = get_args(literal)
    for arg in args:
        if _obj_is_from_typing(obj=arg):
            raise UserWarning(f"enforce_literals does not support nested Literals in 3.8 or before. ({literal})")
        if arg == value:
            return True
    raise AssertionError(f"'{value}' is not in {args} for '{name}'")

def _check_value_to_type(kwargs, name, type_):
    if name not in kwargs:
        return True
    if get_origin(type_) is Literal:
        _check_value_to_literal(kwargs=kwargs, name=name, literal=type_)

def enforce_literals(function):
    kwargs = _getframe(1).f_locals
    for name, type_ in function.__annotations__.items():
        _check_value_to_type(kwargs=kwargs, name=name, type_=type_)




