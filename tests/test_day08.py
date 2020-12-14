from typing import Sequence

from aoc2020.puzzle.day08 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return (
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    )


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 5


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input) == 8
