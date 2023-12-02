from game import Game
from revealed_set import RevealedSet
from color import Color
from game_configuration import GameConfiguration

from infra.game_provider.in_memory import InMemoryGameProvider

from find_possible_games import FindPossibleGames


def test_find_possible_games_with_values_above_and_one_color():
    impossible_game = Game(
        id=1,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 15}),
        ],
    )
    possible_game = Game(
        id=2,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 2}),
        ],
    )

    game_provider = InMemoryGameProvider(games=[possible_game, impossible_game])
    usecase = FindPossibleGames(game_provider=game_provider)
    assert usecase.handle(
        real_game_configuration=GameConfiguration(
            cubes_amount_by_color={Color("red"): 10}
        )
    ) == [possible_game]


def test_find_possible_games_with_values_above_and_multiple_colors():
    impossible_game = Game(
        id=1,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 15}),
            RevealedSet(cubes_amount_by_color={Color("blue"): 4, Color("green"): 3}),
        ],
    )
    possible_game = Game(
        id=2,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 2}),
            RevealedSet(cubes_amount_by_color={Color("blue"): 2, Color("green"): 4}),
        ],
    )

    game_provider = InMemoryGameProvider(games=[possible_game, impossible_game])
    usecase = FindPossibleGames(game_provider=game_provider)
    assert usecase.handle(
        real_game_configuration=GameConfiguration(
            cubes_amount_by_color={
                Color("red"): 10,
                Color("blue"): 10,
                Color("green"): 10,
            }
        )
    ) == [possible_game]


def test_find_possible_games_with_not_represented_color():
    impossible_game = Game(
        id=1,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 15}),
            RevealedSet(cubes_amount_by_color={Color("blue"): 4, Color("green"): 3}),
        ],
    )
    possible_game = Game(
        id=2,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("red"): 2}),
            RevealedSet(cubes_amount_by_color={Color("green"): 4}),
        ],
    )

    game_provider = InMemoryGameProvider(games=[possible_game, impossible_game])
    usecase = FindPossibleGames(game_provider=game_provider)
    assert usecase.handle(
        real_game_configuration=GameConfiguration(
            cubes_amount_by_color={
                Color("red"): 5,
                Color("green"): 5,
            }
        )
    ) == [possible_game]
