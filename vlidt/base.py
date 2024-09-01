from dataclasses import dataclass

from .abc import BaseModelAbc
from .lump import dump_type, collect_sub_dataclasses
from .validation import validate


@dataclass
class BaseModel(BaseModelAbc):
    """Base class for data models that automatically becomes a dataclass."""
    def __post_init__(self):
        validate(self)

    def __init_subclass__(cls, **kwargs):
        # every class has inherite BaseModel make it dataclass
        dataclass(cls)

        cls.__type__ = dump_type(cls)
        cls.__sub_dataclasses__ = collect_sub_dataclasses(cls)


