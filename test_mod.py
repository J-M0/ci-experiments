import pytest

import importlib
import inspect


def get_module_objs(module):
    # return a set of strings that represent the names of objects defined in that module
    return { n for n, o in inspect.getmembers(module, lambda m: inspect.getmodule(m) is module) }


def get_module_all(module):
    return set(getattr(module, '__all__', set()))


def test_exports():
    module = importlib.import_module('mod')

    assert get_module_all(module) == get_module_objs(module)
