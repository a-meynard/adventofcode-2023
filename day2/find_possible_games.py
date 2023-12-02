from game import Game, GameProvider
from revealed_set import RevealedSet
from game_configuration import GameConfiguration


class FindPossibleGames:
    def __init__(self, game_provider: GameProvider) -> None:
        self.game_provider = game_provider

    def __is_valid_revealed_set(
        self, configuration: GameConfiguration, set: RevealedSet
    ) -> bool:
        for color, amount in set.cubes_amount_by_color.items():
            if not (
                color in configuration.cubes_amount_by_color.keys()
                and amount <= configuration.cubes_amount_by_color[color]
            ):
                return False
        return True

    def __is_valid_game(self, configuration: GameConfiguration, game: Game) -> bool:
        for revealed_set in game.revealed_sets:
            if not self.__is_valid_revealed_set(
                configuration=configuration, set=revealed_set
            ):
                return False
        return True

    def handle(self, real_game_configuration: GameConfiguration) -> list[Game]:
        possible_games = []
        for game in self.game_provider.get_all():
            if self.__is_valid_game(configuration=real_game_configuration, game=game):
                possible_games.append(game)
        return possible_games
