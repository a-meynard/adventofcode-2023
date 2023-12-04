from main import Usecase


def test_usecase_solve_first_problem():
    input = []
    assert Usecase().solve_first_problem(puzzle_input=input) == 1
