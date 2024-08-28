from typing_validation import validate as vli
from typing import Generator, Any, Type, Dict
from dataclasses import fields, Field, dataclass, is_dataclass


@dataclass
class BaseModel:
    """Base class for data models that automatically becomes a dataclass."""

    def __init_subclass__(cls, **kwargs):
        # every class has inherite BaseModel make it dataclass
        dataclass(cls)


def iterate_fields(cls: Type[BaseModel]) -> Generator[Any, Field, None]:
    """Yield field values and Field objects for a given dataclass."""
    for fld in fields(cls):
        yield getattr(cls, fld.name), fld


def iterate_fields_type(cls: Type[BaseModel]) -> Generator[Any, Field, None]:
    """Yield field values and their corresponding types from a dataclass."""
    for value, fld in iterate_fields(cls):
        yield getattr(cls, fld.name), fld.type


def validate(cls):
    """Validate each field in a dataclass using the provided validation function."""
    return list(map(
        lambda x: vli(*x),
        iterate_fields_type(cls)
    ))


def dump(dt: Type[BaseModel]) -> Dict:
    """Convert a dataclass instance into a dictionary representation."""
    return {
        fld.name: val if not is_dataclass(val) else dump(val) for val, fld in iterate_fields(dt)
    }


def load(dt: Type[BaseModel], data: Dict) -> BaseModel:
    """Create a dataclass instance from a dictionary representation."""
    kwargs = {
        fld.name: data[fld.name] if not is_dataclass(fld.type) else load(fld.type, data[fld.name])
        for fld in fields(dt)
    }
    return dt(**kwargs)


def dump_type(dt: Type[BaseModel]) -> Dict:
    """Return a dictionary mapping field names to their types for a dataclass."""
    return {
        fld.name: fld.type if not is_dataclass(fld.type) else dump_type(fld.type) for fld in fields(dt)
    }