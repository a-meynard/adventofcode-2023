class Usecase:
    VALID_WORD_FOR_NUMBER = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    def __init__(self) -> None:
        pass

    @staticmethod
    def __extract_all_numbers(line: str, existing_numbers: list[int] = []) -> list[int]:
        next_existing_numbers = existing_numbers.copy()

        if is_a_number(line[0]):
            next_existing_numbers += [int(line[0])]

        for index, valid_word_number in enumerate(Usecase.VALID_WORD_FOR_NUMBER):
            if line.startswith(valid_word_number):
                # NOTE: We add 1 because we start with "one" and not "zero"
                next_existing_numbers += [index + 1]

        if len(line) == 1:
            return next_existing_numbers
        else:
            return Usecase.__extract_all_numbers(line[1:], next_existing_numbers)

    def handle(self, puzzle_input: list[str]) -> int:
        final_number = 0
        for line in puzzle_input:
            all_numbers = Usecase.__extract_all_numbers(line)
            final_number += int(str(all_numbers[0]) + str(all_numbers[-1]))
            # QUESTION: Should we count zero as a valid word ?
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
