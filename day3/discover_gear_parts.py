from schema import Schema
from engine_part import EnginePart


class DiscoverGearParts:
    def __init__(self) -> None:
        pass

    def handle(self, schema: Schema) -> set[EnginePart]:
        gears: set[EnginePart] = set()
        for engine_part in schema.symbols:
            part_number_counter = 0
            for part_number in schema.part_numbers:
                if part_number.is_adjacent_to_symbol(symbol=engine_part):
                    part_number_counter += 1
            if part_number_counter == 2:
                gears.add(engine_part)
        return gears
