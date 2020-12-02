from typing import Sequence

from aoc2020.puzzle.day2 import (
    parse_puzzle_item,
    solve_first_part,
    solve_second_part,
    validate_first_policy,
    validate_second_policy,
)
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return (
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    )


def test_first_part(puzzle_input):
    valid = tuple(validate_first_policy(parse_puzzle_item(x)) for x in puzzle_input)
    assert valid == (True, False, True)
    assert solve_first_part(puzzle_input) == 2


def test_second_part(puzzle_input):
    valid = tuple(validate_second_policy(parse_puzzle_item(x)) for x in puzzle_input)
    assert valid == (True, False, False)
    assert solve_second_part(puzzle_input) == 1
