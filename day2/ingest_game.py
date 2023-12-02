import re

from game import Game
from revealed_set import RevealedSet
from color import Color


class IngestGame:
    def __init__(self) -> None:
        pass

    @staticmethod
    def extract_game_id(game_line: str) -> int:
        m = re.search(r"^Game (\d+):", game_line)
        return int(m.group(1))

    @staticmethod
    def extract_revealed_sets(game_line: str, game_id: int) -> list[RevealedSet]:
        raw_revealed_sets = game_line.removeprefix(f"Game {str(game_id)}: ")

        revealed_sets: list[RevealedSet] = []
        for raw_revealed_set in raw_revealed_sets.split(";"):
            revealed_set = RevealedSet(cubes_amount_by_color={})
            for raw_cube in raw_revealed_set.split(", "):
                m = re.search(r"(\d+) (\w+)", raw_cube)
                revealed_set.cubes_amount_by_color[Color(m.group(2))] = int(m.group(1))
            revealed_sets.append(revealed_set)

        return revealed_sets

    def handle(self, game_line: str) -> Game:
        game_id = IngestGame.extract_game_id(game_line=game_line)
        revealed_sets = IngestGame.extract_revealed_sets(
            game_line=game_line, game_id=game_id
        )
        return Game(id=game_id, revealed_sets=revealed_sets)
