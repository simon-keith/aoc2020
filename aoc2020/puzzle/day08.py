#!/usr/bin/env python
from enum import Enum
from typing import List, Sequence, Tuple

from aoc2020.input import get_puzzle_input


class Operation(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"


def parse_puzzle_input(puzzle_input: Sequence[str]) -> List[Tuple[Operation, int]]:
    splitted = (p.split() for p in puzzle_input)
    return list((Operation(o), int(a)) for o, a in splitted)


def run_boot_code(
    instructions: Sequence[Tuple[Operation, int]],
    return_if_cyclical: bool = False,
) -> int:
    visited = set()
    accumulator = 0
    i = 0
    while i < len(instructions):
        if i in visited:
            if return_if_cyclical:
                return accumulator
            raise RuntimeError("instructions are cyclical")
        visited.add(i)
        operation, argument = instructions[i]
        if operation is Operation.ACC:
            accumulator += argument
        i += argument if operation is Operation.JMP else 1
    return accumulator


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    instructions = parse_puzzle_input(puzzle_input)
    return run_boot_code(instructions, True)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    instructions = parse_puzzle_input(puzzle_input)
    for i in range(len(instructions)):
        operation, argument = instructions[i]
        if operation is Operation.ACC:
            continue
        new_operation = Operation.JMP if operation is Operation.NOP else Operation.NOP
        instructions[i] = new_operation, argument
        try:
            return run_boot_code(instructions)
        except RuntimeError:
            instructions[i] = operation, argument
    raise ValueError("no permutation fixed the instructions")


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day08")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
