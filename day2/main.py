class Usecase:
    def __init__(self) -> None:
        pass

    def handle(self, puzzle_input: str):
        pass


def read_input() -> list[str]:
    filename = "input.txt"
    with open(filename, "r+") as puzzle:
        return puzzle.readlines()


def main():
    puzzle_input = read_input()
    usecase = Usecase()
    print(usecase.handle(puzzle_input=puzzle_input))


if __name__ == "__main__":
    main()
