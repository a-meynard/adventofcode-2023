from schema import Schema
from part_number import PartNumber


class FilterInvalidPartNumber:
    def __init__(self) -> None:
        pass

    def handle(self, schema: Schema) -> set[PartNumber]:
        valid_part_numbers = set()
        for part_number in schema.part_numbers:
            for symbol in schema.symbols:
                if part_number.is_adjacent_to_symbol(symbol=symbol):
                    valid_part_numbers.add(part_number)
                    break
        return valid_part_numbers
