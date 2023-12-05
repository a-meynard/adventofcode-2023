from scratchcard import ScratchCard
from expand_scratchcards import ExpandScratchCards


def test_expand_scratchcards_when_no_worth_value():
    scratchcards = [ScratchCard(id=1, winning_numbers={2}, numbers={10, 15})]
    assert ExpandScratchCards().handle(scratchcards=scratchcards) == [
        ScratchCard(id=1, winning_numbers={2}, numbers={10, 15})
    ]


def test_expand_scratchcards_when_worth_value_of_1():
    scratchcards = [
        ScratchCard(id=1, winning_numbers={10}, numbers={10, 15}),
        ScratchCard(id=2, winning_numbers={2}, numbers={10, 15}),
    ]
    assert ExpandScratchCards().handle(scratchcards=scratchcards) == [
        ScratchCard(id=1, winning_numbers={10}, numbers={10, 15}),
        ScratchCard(id=2, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=2, winning_numbers={2}, numbers={10, 15}),
    ]


def test_expand_scratchcards_when_multiple_worth_values():
    scratchcards = [
        ScratchCard(id=1, winning_numbers={10, 15, 20}, numbers={10, 15, 20, 30}),
        ScratchCard(id=2, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=3, winning_numbers={2}, numbers={2, 15}),
        ScratchCard(id=4, winning_numbers={2}, numbers={10, 15}),
    ]
    assert ExpandScratchCards().handle(scratchcards=scratchcards) == [
        ScratchCard(id=1, winning_numbers={10, 15, 20}, numbers={10, 15, 20, 30}),
        ScratchCard(id=2, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=2, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=3, winning_numbers={2}, numbers={2, 15}),
        ScratchCard(id=3, winning_numbers={2}, numbers={2, 15}),
        ScratchCard(id=4, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=4, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=4, winning_numbers={2}, numbers={10, 15}),
        ScratchCard(id=4, winning_numbers={2}, numbers={10, 15}),
    ]
