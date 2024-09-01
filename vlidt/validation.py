from typing_validation import validate as vli

from .utils import iterate_fields_type


def validate(cls):
    """Validate each field in a dataclass using the provided validation function."""
    return list(map(
        lambda x: vli(*x),
        iterate_fields_type(cls)
    ))
