from ingest_almanac import IngestAlmanac
from search_lowest_location import SearchLowestLocation

from feature_router import FeatureRouter


class Usecase:
    def __init__(self) -> None:
        pass

    def solve_first_problem(self, puzzle_input: list[str]) -> int:
        FeatureRouter.ENABLE_RANGE_SEED = False
        FeatureRouter.ENABLE_CATEGORY_V2 = True
        sanitized_puzzle_input = [line.replace("\n", "") for line in puzzle_input]
        return SearchLowestLocation().handle(
            almanac=IngestAlmanac().ingest(input=sanitized_puzzle_input)
        )

    def solve_second_problem(self, puzzle_input: list[str]):
        FeatureRouter.ENABLE_RANGE_SEED = True
        FeatureRouter.ENABLE_CATEGORY_V2 = True
        sanitized_puzzle_input = [line.replace("\n", "") for line in puzzle_input]
        return SearchLowestLocation().handle2(
            almanac=IngestAlmanac().ingest(input=sanitized_puzzle_input)
        )


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
