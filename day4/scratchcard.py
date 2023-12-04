from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class ScratchCard:
    id: int
    winning_numbers: set[int]
    numbers: set[int]

    def calculate_value(self) -> int:
        worth_numbers = self.numbers.intersection(self.winning_numbers)
        if worth_numbers != set():
            return 2 ** (len(worth_numbers) - 1)
        else:
            return 0
