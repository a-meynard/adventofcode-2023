from ingest_engine_schema import IngestEngineSchema
from filter_invalid_part_number import FilterInvalidPartNumber
from discover_gear_parts import DiscoverGearParts


class Usecase:
    def __init__(self) -> None:
        pass

    def solve_first_problem(self, puzzle_input: list[str]) -> int:
        sanitized_puzzle_input = [line.replace("\n", "") for line in puzzle_input]
        part_numbers = FilterInvalidPartNumber().handle(
            schema=IngestEngineSchema().handle(raw_schema=sanitized_puzzle_input)
        )
        return sum([p.id for p in part_numbers])

    def solve_second_problem(self, puzzle_input: str):
        sanitized_puzzle_input = [line.replace("\n", "") for line in puzzle_input]
        schema = IngestEngineSchema().handle(raw_schema=sanitized_puzzle_input)
        gears = DiscoverGearParts().handle(schema=schema)
        total_gear_power = 0
        for gear in gears:
            gear_power = 1
            for part_number in schema.part_numbers:
                if part_number.is_adjacent_to_symbol(symbol=gear):
                    gear_power *= part_number.id
            total_gear_power += gear_power
        return total_gear_power


def read_input() -> list[str]:
    filename = "input.txt"
    with open(filename, "r+") as puzzle:
        return puzzle.readlines()


def main():
    puzzle_input = read_input()
    usecase = Usecase()
    print(usecase.solve_first_problem(puzzle_input=puzzle_input))
    print(usecase.solve_second_problem(puzzle_input=puzzle_input))


if __name__ == "__main__":
    main()
