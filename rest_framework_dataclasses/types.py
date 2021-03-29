# Some type definitions that can be useful.

import typing

try:
    # Python 3.8 and later
    from typing import Final, Literal, Protocol
except ImportError:
    from typing_extensions import Final, Literal, Protocol


# Note that this doesn't actually work yet (https://stackoverflow.com/a/55240861)
class Dataclass(Protocol):
    __dataclass_fields__: typing.Dict

    def __init__(self, **kwargs):
        pass
