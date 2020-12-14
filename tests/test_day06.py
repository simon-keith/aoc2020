from typing import Sequence

from aoc2020.puzzle.day06 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return (
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    )


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 11


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input) == 6
