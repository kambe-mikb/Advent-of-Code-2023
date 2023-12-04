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
"""

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


def part_1(input: T.Iterable) -> int:
    total = 0
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

    for index, line in enumerate(lines):
        for pn in pn_regex.finditer(line):
            print(f"Candidate Part Number: {pn[0]}")
            print(f"Row above: {schematic[index][pn.start():pn.end()+2]}")
            print(f"Row      : {schematic[index+1][pn.start():pn.end()+2]}")
            print(f"Row below: {schematic[index+2][pn.start():pn.end()+2]}")
            print(f"Row Start match: {schematic[index + 1][pn.start()]} not in \"0123456789.\" = {schematic[index + 1][pn.start()] not in '0123456789.'}")
            print(f"Row End match: {schematic[index + 1][pn.end() + 1]} not in \"0123456789.\" = {schematic[index + 1][pn.end() + 1] not in '0123456789.'}")
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
    return total


if __name__ == "__main__":
    print(f"Result of Part 1 (test) = {part_1(input)}")
    print()
    print(f"Result of Part 1 (data) = {part_1(getInput('Input03.txt'))}")
