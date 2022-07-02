from typing import Literal, Optional, get_args, get_origin, Dict, Union
import inspect
from itertools import chain


def _get_parameters():
    frame = inspect.stack()[2].frame
    *_, parameters = inspect.getargvalues(frame)
    return parameters

def _check_none_typing(arg, obj_not_from_typing):
    try:
        if isinstance(arg, obj_not_from_typing):
            return True
    except TypeError:
        return arg == obj_not_from_typing

def _check_literal(arg, literal):
    return arg in get_args(literal)

def _check_dict(arg, dict_):
    for key, value in arg.items():
        key_type, value_type = get_args(dict_)
        return isinstance(key, key_type) and isinstance(value, value_type)

_CHECKS = {
    None: _check_none_typing,
    Literal: _check_literal,
    Dict: _check_dict,
}

def _check_arg_to_annotations(arg, annotations):
    no_checks_available = True
    for annotation in get_args(annotations):
        origin = get_origin(annotation)
        if origin in _CHECKS:
            no_checks_available = False
            if _CHECKS[origin](arg, annotation):
                return True
    return no_checks_available

def enforce_typing(function):
    parameters = _get_parameters()
    for name, annotations in function.__annotations__.items():
        if name in parameters:
            arg = parameters[name]
            if not _check_arg_to_annotations(arg=arg, annotations=annotations):
                raise TypeError(f"'{arg}' failed annotation of {annotations}")


def enforce_literals(function):
    frame = inspect.stack()[1].frame
    *_, parameters = inspect.getargvalues(frame)
    for name, literal in function.__annotations__.items():
        if get_origin(literal) is Literal and name in parameters:
            value = parameters[name]
            assert value in get_args(literal), f"'{value}' is invalid - valid options are {get_args(literal)}"


