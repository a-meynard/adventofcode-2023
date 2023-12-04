from dataclasses import dataclass

from position import Position
from engine_part import EnginePart


@dataclass(frozen=True, kw_only=True)
class PartNumber:
    # NOTE: For simplicity I do not separate valid and invalid part number. We
    # will filter invalid part number so that they do not appear in future
    # part number sets
    id: int
    position: Position

    def is_on_same_or_surrounding_line_as_symbol(self, symbol: EnginePart) -> bool:
        return (
            symbol.position.line - 1 <= self.position.line <= symbol.position.line + 1
        )

    def is_on_same_or_surrounding_column_as_symbol(self, symbol: EnginePart) -> bool:
        return self.position.start - 1 <= symbol.position.start <= self.position.end + 1

    def is_adjacent_to_symbol(self, symbol: EnginePart) -> bool:
        return self.is_on_same_or_surrounding_column_as_symbol(
            symbol=symbol
        ) and self.is_on_same_or_surrounding_line_as_symbol(symbol=symbol)
