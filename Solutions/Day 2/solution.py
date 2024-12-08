"""
Day 2: Red-Nosed Reports
https://adventofcode.com/2024/day/2
"""

from math import copysign

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
def parse_level(level: str) -> list[int]:
    nums = level.split(" ")
    return [int(num) for num in nums]


def is_safe(nums: list[int]) -> bool:
    initial_sign = copysign(1, nums[0] - nums[1])
    for i in range(len(nums) - 1):
        diff = nums[i] - nums[i + 1]
        sign = copysign(1, diff)
        if not (1 <= abs(diff) <= 3) or sign != initial_sign:
            return False
    return True


def is_fixable(nums: list[int]) -> bool:  # Required for Part 2
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i + 1 :]
        if is_safe(nums=new_nums):
            return True
    return False


def safe_levels(levels: list[str], *, allow_fixable: bool) -> int:
    safe_count = 0
    for row in levels:
        row_parsed = parse_level(level=row)
        if is_safe(nums=row_parsed):
            safe_count += 1
        else:
            if allow_fixable and is_fixable(nums=row_parsed):
                safe_count += 1
    return safe_count


print(safe_levels(levels=input_list, allow_fixable=False))  # Print: 252


# Part 2
print(safe_levels(levels=input_list, allow_fixable=True))  # Print: 324
