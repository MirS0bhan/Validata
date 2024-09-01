from .abc import BaseModelAbc as BaseModel

from typing import Type, Dict
from dataclasses import fields, is_dataclass


def dump(dt: Type[BaseModel]) -> Dict:
    """Convert a dataclass instance into a dictionary representation."""
    kwarg = dt.__dict__.copy()
    for name, typ in dt.__sub_dataclasses__.items():
        kn = kwarg[name]
        if type(kn) is not dict:
            kwarg[name] = dump(kn)
    return kwarg


def load(dt: Type[BaseModel], data: Dict) -> BaseModel:
    """Create a dataclass instance from a dictionary representation."""
    if is_dataclass(data):
        return data
    # Check if the dataclass has fields
    for name, dtcls in dt.__sub_dataclasses__.items():
        data[name] = load(dtcls, data[name])

    return dt(**data)


def dump_type(dt: Type[BaseModel]) -> Dict:
    """Return a dictionary mapping field names to their types for a dataclass."""
    return {
        fld.name: fld.type if not is_dataclass(fld.type) else dump_type(fld.type)
        for fld in fields(dt)
    }


def collect_sub_dataclasses(dt):
    return {
        fld.name: fld.type
        for fld in filter(lambda fld: is_dataclass(fld.type), fields(dt))
    }


