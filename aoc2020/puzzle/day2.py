import re
from typing import Callable, Sequence, Tuple

from aoc2020.input import get_puzzle_input

puzzle_input = get_puzzle_input("day2")
puzzle_pattern = re.compile(
    r"(?P<x1>\d+)-(?P<x2>\d+)\s+(?P<letter>\w{1}):\s+(?P<password>\w+)"
)
PuzzleItemType = Tuple[str, str, int, int]


def parse_puzzle_item(item: str) -> PuzzleItemType:
    match = puzzle_pattern.match(item)
    if match is None:
        raise ValueError(f"'{item}' if not conform")
    x1, x2, letter, password = match.groups()
    x1, x2 = int(x1), int(x2)
    return password, letter, x1, x2


def count_valid_items(
    puzzle_input: Sequence[str], policy_func: Callable[[str, str, int, int], bool]
):
    valid_count = 0
    for item in puzzle_input:
        password, letter, x1, x2 = parse_puzzle_item(item)
        valid_count += policy_func(password, letter, x1, x2)
    return valid_count


def validate_first_policy(password: str, letter: str, x1: int, x2: int) -> bool:
    letter_count = sum(char is letter for char in password)
    return x1 <= letter_count <= x2


def get_char(x: str, i: int):
    try:
        return x[i]
    except IndexError:
        return


def validate_second_policy(password: str, letter: str, x1: int, x2: int) -> bool:
    a, b = get_char(password, x1 - 1), get_char(password, x2 - 1)
    return (a == letter or b == letter) and a != b


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return count_valid_items(puzzle_input, validate_first_policy)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return count_valid_items(puzzle_input, validate_second_policy)


if __name__ == "__main__":
    print(solve_first_part(puzzle_input=puzzle_input))
    print(solve_second_part(puzzle_input=puzzle_input))
