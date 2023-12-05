from scratchcard import ScratchCard
from ingest_scratchcards import IngestScratchCards


def test_ingest_scratchcards_when_one_number_in_each_section():
    input = ["Card 1: 10 | 10"]
    assert IngestScratchCards().handle(raw_scratchcards=input) == [
        ScratchCard(id=1, winning_numbers={10}, numbers={10})
    ]


def test_ingest_scratchcards_with_single_digit_number():
    input = ["Card 1: 10 |  5"]
    assert IngestScratchCards().handle(raw_scratchcards=input) == [
        ScratchCard(id=1, winning_numbers={10}, numbers={5})
    ]


def test_ingest_scratchcards_with_multiple_number_in_each_section():
    input = ["Card 1: 10 32 |  5 10  2"]
    assert IngestScratchCards().handle(raw_scratchcards=input) == [
        ScratchCard(id=1, winning_numbers={10, 32}, numbers={5, 10, 2})
    ]


def test_ingest_scratchcards_with_aligned_card_id():
    input = ["Card   1: 10 32 |  5 10  2"]
    assert IngestScratchCards().handle(raw_scratchcards=input) == [
        ScratchCard(id=1, winning_numbers={10, 32}, numbers={5, 10, 2})
    ]
