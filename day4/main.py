from ingest_scratchcards import IngestScratchCards


class Usecase:
    def __init__(self) -> None:
        pass

    def solve_first_problem(self, puzzle_input: list[str]) -> int:
        sanitized_puzzle_input = [line.replace("\n", "") for line in puzzle_input]
        scratchcards = IngestScratchCards().handle(
            raw_scratchcards=sanitized_puzzle_input
        )
        return sum([s.calculate_value() for s in scratchcards])

    def solve_second_problem(self, puzzle_input: list[str]):
        pass


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
