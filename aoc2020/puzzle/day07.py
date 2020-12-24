#!/usr/bin/env python
import re
from dataclasses import dataclass
from functools import cache
from typing import Callable, Dict, Iterable, Sequence, Tuple

from aoc2020.input import get_puzzle_input
from aoc2020.puzzle import print_puzzle

OUTER_PUZZLE_PATTERN = re.compile(r"([\w\s]+?)\sbags\scontain\s([\w\s,]+?)\.")
INNER_PUZZLE_PATTERN = re.compile(r"(\d+)\s([\w\s]+?)\sbag[s]*")


@dataclass
class Bag:
    color: str
    quantity: int


@dataclass
class Rule:
    color: str
    content: Sequence[Bag]


def parse_inner(inner: str) -> Iterable[Tuple[int, str]]:
    for i in inner.split(", "):
        m = INNER_PUZZLE_PATTERN.match(i)
        if m is not None:
            quantity, color = m.groups()
            yield int(quantity), color


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Dict[str, Rule]:
    outer_generator = (OUTER_PUZZLE_PATTERN.match(p).groups() for p in puzzle_input)
    inner_generator = ((outer, parse_inner(inner)) for outer, inner in outer_generator)
    rule_generator = (
        Rule(
            color=outer_bag,
            content=tuple(Bag(color=c, quantity=int(q)) for q, c in inner_bags),
        )
        for outer_bag, inner_bags in inner_generator
    )
    return {r.color: r for r in rule_generator}


def make_search_func(rules: Dict[str, Rule]) -> Callable[[str, str], bool]:
    @cache
    def outer_contains_inner(outer: str, inner: str) -> bool:
        for bag in rules[outer].content:
            if bag.color == inner or outer_contains_inner(bag.color, inner):
                return True
        return False

    return outer_contains_inner


def make_count_func(rules: Dict[str, Rule]) -> Callable[[str], int]:
    @cache
    def count_contained_bags(outer: str) -> int:
        return sum(
            bag.quantity + count_contained_bags(bag.color) * bag.quantity
            for bag in rules[outer].content
        )

    return count_contained_bags


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    rules = parse_puzzle_input(puzzle_input)
    outer_contains_inner = make_search_func(rules)
    return sum(outer_contains_inner(color, "shiny gold") for color in rules)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    rules = parse_puzzle_input(puzzle_input)
    count_contained_bags = make_count_func(rules)
    return count_contained_bags("shiny gold")


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day07")
    print_puzzle(puzzle_input, solve_first_part, solve_second_part)
