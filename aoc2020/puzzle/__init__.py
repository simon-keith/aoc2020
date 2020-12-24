import time
from typing import Callable, Sequence, Tuple


def solve_puzzle(
    puzzle_input: Sequence[str],
    solve_first_part: Callable[[Sequence[str]], int],
    solve_second_part: Callable[[Sequence[str]], int],
) -> Tuple[Tuple[int, float], Tuple[int, float]]:
    start_time = time.perf_counter()
    first_result = solve_first_part(puzzle_input)
    first_time = time.perf_counter()
    second_result = solve_second_part(puzzle_input)
    second_time = time.perf_counter()
    first_duration = 1000 * (first_time - start_time)
    second_duration = 1000 * (second_time - first_time)
    return (first_result, first_duration), (second_result, second_duration)


def print_puzzle(
    puzzle_input: Sequence[str],
    solve_first_part: Callable[[Sequence[str]], int],
    solve_second_part: Callable[[Sequence[str]], int],
):
    results = solve_puzzle(puzzle_input, solve_first_part, solve_second_part)
    for puzzle, r in zip(("first", "second"), results):
        result, duration = r
        print(f"solved {puzzle} part in {duration:.3f} ms: {result}")
