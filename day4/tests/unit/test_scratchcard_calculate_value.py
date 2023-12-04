from scratchcard import ScratchCard


def test_scratchcard_calculate_value_when_no_winning_numbers():
    assert (
        ScratchCard(
            id=1, winning_numbers={10, 25, 30}, numbers={5, 15, 42, 67}
        ).calculate_value()
        == 0
    )


def test_scratchcard_calculate_value_when_one_winning_number():
    assert (
        ScratchCard(
            id=1, winning_numbers={10, 25, 30}, numbers={5, 25, 42, 67}
        ).calculate_value()
        == 1
    )


def test_scratchcard_calculate_value_when_multiple_winning_numbers():
    assert (
        ScratchCard(
            id=1, winning_numbers={10, 25, 30}, numbers={5, 25, 30, 10}
        ).calculate_value()
        == 4
    )
