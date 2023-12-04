from dataclasses import dataclass

from engine_part import EnginePart
from part_number import PartNumber


@dataclass(kw_only=True)
class Schema:
    symbols: set[EnginePart]
    part_numbers: set[PartNumber]
