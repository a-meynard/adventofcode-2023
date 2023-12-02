from dataclasses import dataclass

from color import Color


@dataclass()
class RevealedSet:
    cubes_amount_by_color: dict[Color, int]
