from main import Usecase


def test_usecase_with_simple_input():
    input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert Usecase().solve_first_problem(puzzle_input=input) == 4361


def test_usecase_solve_second_problem():
    input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert Usecase().solve_second_problem(puzzle_input=input) == 467835
