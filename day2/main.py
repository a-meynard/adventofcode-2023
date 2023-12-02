from infra.game_provider.ingest_game import IngestGameGameProvider

from find_possible_games import FindPossibleGames
from game_configuration import GameConfiguration
from color import Color


class Usecase:
    def __init__(self) -> None:
        pass

    def handle(self, puzzle_input: str):
        possible_games = FindPossibleGames(
            game_provider=IngestGameGameProvider(game_lines=puzzle_input)
        ).handle(
            real_game_configuration=GameConfiguration(
                cubes_amount_by_color={
                    Color("red"): 12,
                    Color("green"): 13,
                    Color("blue"): 14,
                }
            )
        )
        return sum([game.id for game in possible_games])


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
