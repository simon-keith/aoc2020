from typing import Iterable, Sequence, Tuple

from aoc2020.input import get_puzzle_input

puzzle_input = get_puzzle_input("day1")


def parse_puzzle_input(puzzle_input: Tuple[str]) -> Tuple[int]:
    return tuple(int(x) for x in puzzle_input)


def iter_pairs_with_sum(
    integers: Sequence[int], target_sum: int
) -> Iterable[Tuple[int, int]]:
    integer_set = set()
    for i in integers:
        diff = target_sum - i
        if diff in integer_set:
            yield diff, i
        integer_set.add(i)


def solve_first_puzzle(puzzle_input: Tuple[str], *, target_sum: int = 2020) -> int:
    integers = parse_puzzle_input(puzzle_input)
    try:
        a, b = next(iter_pairs_with_sum(integers=integers, target_sum=target_sum))
    except StopIteration:
        raise ValueError(f"found no pair that sum to {target_sum}")
    return a * b


if __name__ == "__main__":
    print(solve_first_puzzle(puzzle_input=puzzle_input))
