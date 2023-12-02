from game import Game
from game_configuration import GameConfiguration


class FindMinimalGameConfiguration:
    def __init__(self) -> None:
        pass

    def handle(self, game: Game) -> GameConfiguration:
        game_configuration = GameConfiguration(cubes_amount_by_color={})
        for set in game.revealed_sets:
            for color, amount in set.cubes_amount_by_color.items():
                if game_configuration.cubes_amount_by_color.get(color, 0) < amount:
                    game_configuration.cubes_amount_by_color[color] = amount
        return game_configuration
