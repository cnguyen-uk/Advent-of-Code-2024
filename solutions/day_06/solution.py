"""
Day 6: Guard Gallivant
https://adventofcode.com/2024/day/6
"""

from collections import Counter
from typing import TypedDict

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
def is_valid_position(position: tuple[int, int], situation_map: list[str]) -> bool:
    row_count, column_count = len(situation_map), len(situation_map[0])
    (row, column) = position
    return row >= row_count or row < 0 or column >= column_count or column < 0


class PositionInformation(TypedDict):
    position: tuple[int, int]
    orientation: str


def next_step(orientation: str, position: tuple[int, int], situation_map: list[str]) -> PositionInformation:
    (row, column) = position
    position_next = {
        "^": (row - 1, column),
        ">": (row, column + 1),
        "v": (row + 1, column),
        "<": (row, column - 1),
    }
    orientation_next = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }
    next_intended_step = position_next[orientation]
    if not is_valid_position(position=next_intended_step, situation_map=situation_map):
        return {"position": position, "orientation": orientation}  # Next step would be out of bounds, so stay still
    while situation_map[next_intended_step[0]][next_intended_step[1]] in ["#", "O"]:
        orientation = orientation_next[orientation]
        next_intended_step = position_next[orientation]

    return {"position": next_intended_step, "orientation": orientation}


def starting_position(starting_orientation: str, situation_map: list[str]) -> tuple[int, int]:
    for row, row_contents in enumerate(situation_map):
        if starting_orientation in row_contents:
            return row, row_contents.index(starting_orientation)
    raise ValueError(f"No {starting_orientation} found in situation_map.")


def path_is_loop(path: list[tuple[int, int]]) -> bool:
    positions_count = Counter(path)
    most_common_positions = positions_count.most_common(n=5)
    repetition = 5  # Path is probably a loop if any position is visited more than 5 times
    return any(position[1] > repetition for position in most_common_positions)


class PathMetadata(TypedDict):
    positions: list[tuple[int, int]]
    is_loop: bool


def path_metadata(starting_orientation: str, situation_map: list[str]) -> PathMetadata:
    positions = []
    position = starting_position(starting_orientation=starting_orientation, situation_map=situation_map)
    positions.append(position)
    orientation = starting_orientation
    is_loop = False
    while next_step(orientation=orientation, position=position, situation_map=situation_map)["position"] != position:
        if not path_is_loop(path=positions):
            next_position = next_step(orientation=orientation, position=position, situation_map=situation_map)
            position = next_position["position"]
            orientation = next_position["orientation"]
            positions.append(position)
        else:
            is_loop = True
            break
    return {"positions": positions, "is_loop": is_loop}


final_path = path_metadata(starting_orientation="^", situation_map=input_list)
print(len(set(final_path["positions"])))  # Print: 4656


# Part 2
def obstruction_positions(starting_orientation: str, situation_map: list[str]) -> list[tuple[int, int]]:
    start_position = starting_position(starting_orientation=starting_orientation, situation_map=input_list)
    obstructions = []
    for position in set(final_path["positions"]):
        if position != start_position:
            row, column = position[0], position[1]

            original_row_contents = situation_map[row]
            new_row_contents = original_row_contents[:column] + "O" + original_row_contents[column + 1 :]

            new_situation_map = situation_map.copy()
            new_situation_map[row] = new_row_contents
            new_path = path_metadata(starting_orientation=starting_orientation, situation_map=new_situation_map)
            if new_path["is_loop"]:
                obstructions.append(position)
    return obstructions


print(len(obstruction_positions(starting_orientation="^", situation_map=input_list)))  # Print: 1575
# Code took 2:21:06.978517 to run.
# Changing path_is_loop to check for 3 position re-visits instead of 5 runs in 1:47:02.218072,
# but gives a wrong answer of 1587.
