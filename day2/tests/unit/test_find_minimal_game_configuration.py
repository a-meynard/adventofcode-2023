from game import Game
from revealed_set import RevealedSet
from color import Color
from game_configuration import GameConfiguration

from find_minimal_game_configuration import FindMinimalGameConfiguration


def test_find_minimal_game_configuration_with_multiple_color():
    game = Game(
        id=1,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 5}),
            RevealedSet(cubes_amount_by_color={Color("blue"): 3}),
            RevealedSet(cubes_amount_by_color={Color("red"): 15}),
        ],
    )
    usecase = FindMinimalGameConfiguration()
    assert usecase.handle(game=game) == GameConfiguration(
        cubes_amount_by_color={Color("red"): 15, Color("blue"): 3}
    )
