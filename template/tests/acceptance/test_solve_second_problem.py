from main import Usecase


def test_usecase_solve_second_problem():
    input = []
    assert Usecase().solve_second_problem(puzzle_input=input) == 1
