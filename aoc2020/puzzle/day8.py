#!/usr/bin/env python

from enum import Enum
from typing import Sequence, Tuple

from aoc2020.input import get_puzzle_input


class Operation(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[Tuple[Operation, int]]:
    splitted = (p.split() for p in puzzle_input)
    return tuple((Operation(o), int(a)) for o, a in splitted)


def run_boot_code(instructions: Sequence[Tuple[Operation, int]]) -> int:
    ran = set()
    accumulator = 0
    i = 0
    while i < len(instructions):
        if i in ran:
            break
        operation, argument = instructions[i]
        if operation is Operation.JMP:
            inc = argument
        else:
            if operation is Operation.ACC:
                accumulator += argument
            inc = 1
        ran.add(i)
        i += inc
    return accumulator


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    instructions = parse_puzzle_input(puzzle_input)
    return run_boot_code(instructions)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day8")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
