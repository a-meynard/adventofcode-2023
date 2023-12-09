from dataclasses import dataclass, field

from category import Category


@dataclass
class Almanac:
    initial_seeds: list[int] = field(default_factory=list)
    categories: list[Category] = field(default_factory=list)
