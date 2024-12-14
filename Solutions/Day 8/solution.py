"""
Day 8: Resonant Collinearity
https://adventofcode.com/2024/day/8
"""

import itertools

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
def antinode_points(point_1: tuple[int, int], point_2: tuple[int, int]) -> list[tuple[int, int]]:
    row_1, column_1 = point_1
    row_2, column_2 = point_2
    antipode_point_1 = (2 * row_1 - row_2, 2 * column_1 - column_2)
    antipode_point_2 = (2 * row_2 - row_1, 2 * column_2 - column_1)
    return [antipode_point_1, antipode_point_2]


def antenna_positions(antenna_map: list[str]) -> dict[str, list[tuple[int, int]]]:
    positions: dict[str, list[tuple[int, int]]] = {}
    for i, row in enumerate(antenna_map):
        for j, column in enumerate(row):
            if column != ".":
                position = (i, j)
                positions.setdefault(column, []).append(position)
    return positions


def is_valid_position(position: tuple[int, int], location_map: list[str]) -> bool:
    row_count, column_count = len(location_map), len(location_map[0])
    (row, column) = position
    return not (row >= row_count or row < 0 or column >= column_count or column < 0)


def antinode_positions(antenna_map: list[str]) -> list[tuple[int, int]]:
    positions = []
    antenna_data = antenna_positions(antenna_map=antenna_map)
    for antenna in antenna_data:
        antenna_locations = antenna_data[antenna]
        location_pair_combinations = itertools.combinations(antenna_locations, 2)
        antinode_locations = [antinode_points(point_1, point_2) for point_1, point_2 in location_pair_combinations]
        antinode_locations_flattened = [item for sublist in antinode_locations for item in sublist]
        positions.extend(antinode_locations_flattened)
    positions = [position for position in positions if is_valid_position(position=position, location_map=antenna_map)]
    return list(set(positions))


print(len(set(antinode_positions(antenna_map=input_list))))  # Print: 351

# Part 2
