from dataclasses import dataclass

from typing import ClassVar


@dataclass(frozen=True)
class Color:
    color: str

    VALID_COLORS: ClassVar[set[str]] = {"red", "green", "blue"}

    def __post_init__(self):
        if self.color not in Color.VALID_COLORS:
            raise ValueError("Unknown color")
