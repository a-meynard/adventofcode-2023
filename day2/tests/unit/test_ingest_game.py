import pytest

from game import Game
from revealed_set import RevealedSet
from color import Color

from ingest_game import IngestGame


def test_ingest_game_with_one_revealed_set():
    example = "Game 1: 3 blue, 4 red"
    assert IngestGame().handle(game_line=example) == Game(
        id=1,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("blue"): 3, Color("red"): 4}),
        ],
    )


def test_ingest_game_with_multiple_revealed_set():
    example = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert IngestGame().handle(game_line=example) == Game(
        id=1,
        revealed_sets=[
            RevealedSet(cubes_amount_by_color={Color("blue"): 3, Color("red"): 4}),
            RevealedSet(
                cubes_amount_by_color={
                    Color("red"): 1,
                    Color("green"): 2,
                    Color("blue"): 6,
                }
            ),
            RevealedSet(cubes_amount_by_color={Color("green"): 2}),
        ],
    )


def test_ingest_game_with_unknown_color_should_raise_error():
    with pytest.raises(ValueError):
        IngestGame().handle(game_line="Game 1: 3 yellow")
