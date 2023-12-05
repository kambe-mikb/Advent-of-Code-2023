#!/bin/env python
"""
==================
Day """

import typing as T


__author__ = "kambe-mikb"
__all__ = ["getInput"]


def getInput(infile: str) -> T.Generator:
    return (v.rstrip("\n") for v in open(infile))


input = [
]


def part_1(input: T.Iterable) -> int:
    total = 0
    return total


def part_2(input: T.Iterable) -> int:
    total = 0
    return total


if __name__ == "__main__":
    puzzle_input = "Input00.txt"
    print(f"Result of Part 1 (test) = {part_1(input)}")
    # print()
    # print(f"Result of Part 1 (data) = {part_1(getInput(puzzle_input))}")
    # print()
    # print(f"Result of Part 2 (test) = {part_2(input)}")
    # print()
    # print(f"Result of Part 2 (data) = {part_2(getInput(puzzle_input))}")
