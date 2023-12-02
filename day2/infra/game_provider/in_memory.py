from game import Game, GameProvider


class InMemoryGameProvider(GameProvider):
    def __init__(self, games: list[Game]) -> None:
        self.games = games

    def get_all(self) -> list[Game]:
        return self.games
