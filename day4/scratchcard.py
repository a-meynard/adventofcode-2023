from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ScratchCard:
    id: int
    winning_numbers: set[int]
    numbers: set[int]

    __worth_value: int = field(init=False, compare=False, default=0)

    def worth_value(self) -> int:
        if self.__worth_value == 0:
            self.__worth_value = len(self.numbers.intersection(self.winning_numbers))
        return self.__worth_value

    def calculate_value(self) -> int:
        worth_numbers = self.numbers.intersection(self.winning_numbers)
        if worth_numbers != set():
            return 2 ** (len(worth_numbers) - 1)
        else:
            return 0
