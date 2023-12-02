from game import Game, GameProvider

from ingest_game import IngestGame


class IngestGameGameProvider(GameProvider):
    def __init__(self, game_lines: list[str]) -> None:
        self.__ingest_game = IngestGame()
        self.__game_lines = game_lines

    def get_all(self) -> list[Game]:
        return [self.__ingest_game.handle(game_line=g) for g in self.__game_lines]
