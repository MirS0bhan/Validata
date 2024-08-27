from dataclasses import dataclass, fields

from typing_validation import validate


@dataclass
class BaseModel:
    def __post_init__(self):
        for f in fields(self):
            val = self.__dict__[f.name]
            validate(val, f.type)

    def __init_subclass__(cls, **kwargs):
        dataclass(cls)
