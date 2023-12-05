#!/bin/env python
"""
==================
Day 3: Gear Ratios
==================

You and the Elf eventually reach a gondola lift station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of
the engine. There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally, is a "part
number" and should be included in your sum. (Periods (.) do not count as a
symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number
is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?

Your puzzle answer was 531932.

Part Two
========

The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong?
Fortunately, the gondola has a phone labeled "help", so you pick it up and the
engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving with
the other. You're going so slowly that you haven't even left the station. You
exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its
gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so
that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has
part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the
lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear
because it is only adjacent to one part number.) Adding up all of the gear
ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer is 73646890.
"""

from itertools import pairwise
from re import compile
import typing as T


__author__ = "kambe-mikb"
__all__ = ["getInput"]


def getInput(infile: str) -> T.Generator:
    return (v.rstrip("\n") for v in open(infile))


input = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


pn_regex = compile(r"\d+")
symbol_regex = compile(r"[^\d.]")
star_regex = compile(r"\*")


def get_schematic(input: T.Iterable) -> list:
    lines = [line for line in input]
    schematic = (
        ["." * (len(lines[0]) + 2)]
        + [f".{line}." for line in lines]
        + ["." * (len(lines[-1]) + 2)]
    )

    print("+" + ("-" * len(schematic[0])) + "+")
    for row in schematic:
        print(f"|{row}|")
    print("+" + ("-" * len(schematic[-1])) + "+")
    return schematic


def part_1(input: T.Iterable) -> int:
    total = 0
    schematic = get_schematic(input)

    for index, line in enumerate(schematic[1:-1]):
        for pn in pn_regex.finditer(line[1:-1]):
            print(f"Candidate Part Number: {pn[0]}")
            print(f"Row above: {schematic[index][pn.start():pn.end()+2]}")
            print(f"Row      : {schematic[index+1][pn.start():pn.end()+2]}")
            print(f"Row below: {schematic[index+2][pn.start():pn.end()+2]}")
            if any(
                [
                    symbol_regex.search(
                        schematic[index], pn.start(), pn.end() + 2
                    ),
                    schematic[index + 1][pn.start()] not in "0123456789.",
                    schematic[index + 1][pn.end() + 1] not in "0123456789.",
                    symbol_regex.search(
                        schematic[index + 2], pn.start(), pn.end() + 2
                    ),
                ]
            ):
                print(f"Match: Part Number #{pn[0]}")
                total += int(pn[0])
    return total


def part_2(input: T.Iterable) -> int:
    total = 0
    schematic = get_schematic(input)

    for row, star_line in enumerate(schematic):
        for star in star_regex.finditer(star_line):
            column = star.start()
            adj = [
                int(pn[0])
                for pn_row, pn_line in enumerate(
                    schematic[(row - 1) : (row + 2)], row - 1
                )
                for pn in pn_regex.finditer(pn_line)
                if pn.end() >= column and pn.start() <= column + 1
            ]
            for i, j in pairwise(adj):
                total += i * j

    return total


if __name__ == "__main__":
    print(f"Result of Part 1 (test) = {part_1(input)}")
    print()
    print(f"Result of Part 1 (data) = {part_1(getInput('Input03.txt'))}")
    print()
    print(f"Result of Part 2 (test) = {part_2(input)}")
    print()
    print(f"Result of Part 2 (data) = {part_2(getInput('Input03.txt'))}")
