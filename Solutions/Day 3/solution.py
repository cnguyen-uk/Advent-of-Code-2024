"""
Day 3: Mull It Over
https://adventofcode.com/2024/day/3
"""

import re

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()

full_input = "".join(input_list)


# Part 1
def mul(x: int, y: int) -> int:  # Required for future eval() calls to work
    return x * y


def multiply_instructions(instructions: str, *, allow_toggling: bool) -> list[str]:
    match_list = []
    if allow_toggling:  # Required for Part 2
        pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, instructions)

        multiplying_enabled = True
        for match in matches:
            if match == "do()":
                multiplying_enabled = True
            elif match == "don't()":
                multiplying_enabled = False
            elif multiplying_enabled and match.startswith("mul("):
                match_list.append(match)
    else:
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, instructions)
        match_list.extend(matches)
    return match_list


print(sum([eval(i) for i in multiply_instructions(instructions=full_input, allow_toggling=False)]))  # Print: 182780583


# Part 2
print(sum([eval(i) for i in multiply_instructions(instructions=full_input, allow_toggling=True)]))  # Print: 90772405
