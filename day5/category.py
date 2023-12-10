from dataclasses import dataclass


@dataclass
class Category:
    name: str
    number: int
    destination_numer: int

    def get_to_destination(self, number: int) -> int:
        if self.number == number:
            return self.destination_numer
        else:
            return number


@dataclass
class CategoryV2:
    name: str
    source_start: int
    destination_start: int
    range_length: int

    def get_to_destination(self, number: int) -> int:
        if self.source_start <= number < self.source_start + self.range_length:
            return self.destination_start + (number - self.source_start)
        else:
            return number

    def get_to_source(self, number: int) -> int:
        if (
            self.destination_start
            <= number
            < self.destination_start + self.range_length
        ):
            return self.source_start + (number - self.destination_start)
        else:
            return number
