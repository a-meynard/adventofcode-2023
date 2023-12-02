from main import Usecase


def test_usecase_with_one_line_with_digit_at_each_ends():
    assert Usecase().handle(["1abc2"]) == 12


def test_usecase_with_one_line_with_in_the_middle():
    assert Usecase().handle(["pqr3stu8vwx"]) == 38


def test_usecase_with_one_number_on_the_line():
    assert Usecase().handle(["treb7uchet"]) == 77


def test_usecase_with_more_than_two_number_on_the_line():
    assert Usecase().handle(["a1b2c3d4e5f"]) == 15


def test_usecase_add_multiple_line_number():
    assert Usecase().handle(["pqr3stu8vwx", "1abc2"]) == 50
