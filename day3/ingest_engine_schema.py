from typing import Optional

from engine_part import EnginePart
from schema import Schema
from part_number import PartNumber
from position import Position


def is_a_number(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        pass
    return False


class IngestEngineSchema:
    VALID_SYMBOLS = [i for i in r'\/:*?"<>|#+$&@%=-']
    GEAR_SYMBOL = "*"

    def __init__(self) -> None:
        pass

    def handle(self, raw_schema: list[str]) -> Schema:
        engine_parts: set[EnginePart] = set()
        part_numbers: set[PartNumber] = set()
        current_potential_part_number: Optional[PartNumber] = None

        for y, line in enumerate(raw_schema):
            for x, char in enumerate(line):
                if char == ".":
                    if current_potential_part_number is not None:
                        part_numbers.add(current_potential_part_number)
                        current_potential_part_number = None
                elif is_a_number(char=char):
                    if current_potential_part_number is not None:
                        current_potential_part_number = PartNumber(
                            id=int(
                                line[
                                    current_potential_part_number.position.start : x + 1
                                ]
                            ),
                            position=Position(
                                start=current_potential_part_number.position.start,
                                end=x,
                                line=y,
                            ),
                        )
                    else:
                        current_potential_part_number = PartNumber(
                            id=int(char), position=Position(start=x, end=x, line=y)
                        )
                elif char in IngestEngineSchema.VALID_SYMBOLS:
                    if current_potential_part_number is not None:
                        part_numbers.add(current_potential_part_number)
                        current_potential_part_number = None
                    if char == IngestEngineSchema.GEAR_SYMBOL:
                        engine_parts.add(
                            EnginePart(
                                position=Position(start=x, end=x, line=y), is_gear=True
                            )
                        )
                    else:
                        engine_parts.add(
                            EnginePart(position=Position(start=x, end=x, line=y))
                        )
                else:
                    raise ValueError(f"Found an unknown character, got: '{char}'")
            if current_potential_part_number is not None:
                part_numbers.add(current_potential_part_number)
                current_potential_part_number = None
        return Schema(symbols=engine_parts, part_numbers=part_numbers)
