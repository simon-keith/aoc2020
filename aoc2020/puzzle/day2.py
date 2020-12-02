import re
from dataclasses import dataclass
from typing import Callable, Optional, Sequence

from aoc2020.input import get_puzzle_input

puzzle_input = get_puzzle_input("day2")
puzzle_pattern = re.compile(
    r"(?P<x1>\d+)-(?P<x2>\d+)\s+(?P<letter>\w{1}):\s+(?P<password>\w+)"
)


@dataclass
class PuzzleItem:
    password: str
    letter: str
    x1: int
    x2: int


def parse_puzzle_item(item: str) -> PuzzleItem:
    match = puzzle_pattern.match(item)
    if match is None:
        raise ValueError(f"'{item}' is not conform")
    x1, x2, letter, password = match.groups()
    x1, x2 = int(x1), int(x2)
    return PuzzleItem(password, letter, x1, x2)


def count_valid_items(
    puzzle_input: Sequence[str], policy_func: Callable[[PuzzleItem], bool]
):
    valid_count = 0
    for raw_item in puzzle_input:
        item = parse_puzzle_item(raw_item)
        valid_count += policy_func(item)
    return valid_count


def validate_first_policy(item: PuzzleItem) -> bool:
    letter_count = sum(char is item.letter for char in item.password)
    return item.x1 <= letter_count <= item.x2


def get_char(x: str, one_based_index: int) -> Optional[str]:
    zero_based_index = one_based_index - 1
    try:
        return x[zero_based_index]
    except IndexError:
        return


def validate_second_policy(item: PuzzleItem) -> bool:
    a, b = get_char(item.password, item.x1), get_char(item.password, item.x2)
    return (a == item.letter or b == item.letter) and a != b


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return count_valid_items(puzzle_input, validate_first_policy)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return count_valid_items(puzzle_input, validate_second_policy)


if __name__ == "__main__":
    print(solve_first_part(puzzle_input=puzzle_input))
    print(solve_second_part(puzzle_input=puzzle_input))
