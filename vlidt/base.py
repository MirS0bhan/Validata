from typing_validation import validate as vli

from typing import Generator, Any, Type, Dict
from dataclasses import fields, Field, dataclass, is_dataclass


@dataclass
class BaseModel:
    def __init_subclass__(cls, **kwargs):
        dataclass(cls)


def iterate_fields(cls: Type[BaseModel]) -> Generator[Any, Field, None]:
    for fld in fields(cls):
        yield getattr(cls, fld.name), fld


def iterate_fields_type(cls: Type[BaseModel]) -> Generator[Any, Field, None]:
    for value, fld in iterate_fields(cls):
        yield getattr(cls, fld.name), fld.type


def validate(cls):
    return list(map(
        lambda x: vli(*x),
        iterate_fields_type(cls)
    ))


def dump(dt: Type[BaseModel]) -> Dict:
    return {
        fld.name: val if not is_dataclass(val) else dump(val) for val, fld in iterate_fields(dt)
    }


def load(dt: Type[BaseModel], data: Dict) -> BaseModel:
    kwargs = {
        fld.name: data[fld.name] if not is_dataclass(fld.type) else load(fld.type, data[fld.name])
        for fld in fields(dt)
    }
    return dt(**kwargs)


def dump_type(dt: Type[BaseModel]) -> Dict:
    return {
        fld.name: fld.type if not is_dataclass(fld.type) else dump_type(fld.type) for fld in fields(dt)
    }
