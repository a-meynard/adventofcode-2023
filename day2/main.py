from infra.game_provider.ingest_game import IngestGameGameProvider

from find_possible_games import FindPossibleGames
from game_configuration import GameConfiguration
from color import Color
from ingest_game import IngestGame
from find_minimal_game_configuration import FindMinimalGameConfiguration


class Usecase:
    def __init__(self) -> None:
        pass

    def handle(self, puzzle_input: list[str]):
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

    def handle_second_problem(self, puzzle_input: list[str]) -> int:
        ingest_game = IngestGame()
        total_power = 0
        for game_line in puzzle_input:
            game_configuration = FindMinimalGameConfiguration().handle(
                game=ingest_game.handle(game_line=game_line)
            )
            power = 1
            for amount in game_configuration.cubes_amount_by_color.values():
                power *= amount
            total_power += power
        return total_power


def read_input() -> list[str]:
    filename = "input.txt"
    with open(filename, "r+") as puzzle:
        return puzzle.readlines()


def main():
    puzzle_input = read_input()
    usecase = Usecase()
    print(usecase.handle(puzzle_input=puzzle_input))
    print(usecase.handle_second_problem(puzzle_input=puzzle_input))


if __name__ == "__main__":
    main()
