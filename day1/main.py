class Usecase:
    def __init__(self) -> None:
        pass

    @staticmethod
    def __find_first_number(line: str) -> str:
        for char in line:
            if is_a_number(char):
                return char

    def handle(self, puzzle_input: list[str]) -> int:
        final_number = 0
        for line in puzzle_input:
            built_number = ""
            built_number += Usecase.__find_first_number(line=line)
            built_number += Usecase.__find_first_number(line=reversed(line))
            final_number += int(built_number)
        return final_number


def is_a_number(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        pass
    return False


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
