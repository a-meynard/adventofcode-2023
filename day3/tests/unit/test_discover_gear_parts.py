from schema import Schema
from engine_part import EnginePart
from position import Position
from part_number import PartNumber

from discover_gear_parts import DiscoverGearParts


def test_discover_gear_parts():
    schema = Schema(
        symbols={EnginePart(position=Position(start=2, end=2, line=0), is_gear=True)},
        part_numbers={
            PartNumber(id=12, position=Position(start=0, end=1, line=0)),
            PartNumber(id=12, position=Position(start=3, end=4, line=0)),
        },
    )
    assert DiscoverGearParts().handle(schema=schema) == {
        EnginePart(position=Position(start=2, end=2, line=0), is_gear=True)
    }
