# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from contextlib import contextmanager
import os
from typing import Iterator


class RaiseImportError:
    @classmethod
    @contextmanager
    def module_name(cls, module_name: str) -> Iterator[None]:
        original_value = os.environ.get("RAISE_IMPORT_ERROR", None)
        os.environ["RAISE_IMPORT_ERROR"] = module_name
        try:
            yield
        finally:
            if original_value is None:
                os.environ.pop("RAISE_IMPORT_ERROR", None)
            else:
                os.environ["RAISE_IMPORT_ERROR"] = original_value

    @staticmethod
    def overwrite_imports() -> None:
        builtins = globals()["__builtins__"]

        def overwrite_import(original_import_builtin):
            def import_replacement(name, *args, **kwargs):
                module_name = os.environ.get("RAISE_IMPORT_ERROR", None)
                if name == module_name:
                    raise ImportError(f"{module_name} is not available")
                return original_import_builtin(name, *args, **kwargs)

            return import_replacement

        builtins["__import__"] = overwrite_import(builtins["__import__"])
