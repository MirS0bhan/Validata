from typing import Generator, Any, Type
from dataclasses import fields, Field


def iterate_fields(cls) -> Generator[Any, Field, None]:
    """Yield field values and Field objects for a given dataclass."""
    for fld in fields(cls):
        fld.compare
        yield getattr(cls, fld.name), fld


def iterate_fields_type(cls) -> Generator[Any, Field, None]:
    """Yield field values and their corresponding types from a dataclass."""
    for value, fld in iterate_fields(cls):
        yield getattr(cls, fld.name), fld.type
