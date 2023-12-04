from position import Position
from part_number import PartNumber
from engine_part import EnginePart
from schema import Schema

from filter_invalid_part_number import FilterInvalidPartNumber


def test_is_adjacent_to_symbol_with_invalid_part_number():
    invalid_part_number = PartNumber(id=43, position=Position(start=2, end=3, line=1))
    assert not invalid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=0, end=0, line=0))
    )


def test_is_adjacent_to_symbol_with_valid_part_number_after_symbol():
    valid_part_number = PartNumber(id=438, position=Position(start=1, end=3, line=0))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=0, end=0, line=0))
    )


def test_is_adjacent_to_symbol_with_valid_part_number_before_symbol():
    valid_part_number = PartNumber(id=438, position=Position(start=1, end=3, line=0))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=4, end=4, line=0))
    )


def test_is_adjacent_to_symbol_with_one_digit_valid_part_number_above_symbol():
    valid_part_number = PartNumber(id=4, position=Position(start=3, end=3, line=0))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=3, end=3, line=1))
    )


def test_is_adjacent_to_symbol_with_one_digit_valid_part_number_under_symbol():
    valid_part_number = PartNumber(id=4, position=Position(start=3, end=3, line=2))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=3, end=3, line=1))
    )


def test_is_adjacent_to_symbol_with_large_valid_part_number_above_symbol():
    valid_part_number = PartNumber(id=438, position=Position(start=1, end=3, line=0))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=3, end=3, line=1))
    )


def test_is_adjacent_to_symbol_with_large_valid_part_number_under_symbol():
    valid_part_number = PartNumber(id=438, position=Position(start=1, end=3, line=2))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=2, end=2, line=1))
    )


def test_is_adjacent_to_symbol_with_valid_part_number_in_diagonale_left_and_above_symbol():
    valid_part_number = PartNumber(id=43, position=Position(start=1, end=2, line=0))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=3, end=3, line=1))
    )


def test_is_adjacent_to_symbol_with_valid_part_number_in_diagonale_right_and_above_symbol():
    valid_part_number = PartNumber(id=43, position=Position(start=1, end=2, line=0))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=0, end=0, line=1))
    )


def test_is_adjacent_to_symbol_with_valid_part_number_in_diagonale_left_and_under_symbol():
    valid_part_number = PartNumber(id=43, position=Position(start=1, end=2, line=2))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=3, end=3, line=1))
    )


def test_is_adjacent_to_symbol_with_valid_part_number_in_diagonale_right_and_under_symbol():
    valid_part_number = PartNumber(id=438, position=Position(start=1, end=2, line=2))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=0, end=0, line=1))
    )


def test_is_adjacent_to_symbol_with_very_large_valid_part_number_under_symbol():
    valid_part_number = PartNumber(id=4388, position=Position(start=0, end=4, line=2))
    assert valid_part_number.is_adjacent_to_symbol(
        symbol=EnginePart(position=Position(start=2, end=2, line=1))
    )


def test_filter_invalid_part_number_with_multiple_part_number():
    assert FilterInvalidPartNumber().handle(
        schema=Schema(
            symbols={EnginePart(position=Position(start=2, end=2, line=1))},
            part_numbers={
                PartNumber(id=438, position=Position(start=1, end=3, line=0)),
                PartNumber(id=4, position=Position(start=2, end=2, line=3)),
                PartNumber(id=4598, position=Position(start=3, end=6, line=2)),
            },
        )
    ) == {
        PartNumber(id=438, position=Position(start=1, end=3, line=0)),
        PartNumber(id=4598, position=Position(start=3, end=6, line=2)),
    }
