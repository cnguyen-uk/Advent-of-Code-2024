"""
Day 9: Disk Fragmenter
https://adventofcode.com/2024/day/9
"""

from typing import Any

with open("input.txt") as input_file:
    input_txt = input_file.read()


# Part 1
def disk_map_to_blocks(disk_map: str) -> list[int | None]:
    blocks = []
    id_number = 0
    for i, block_size in enumerate(disk_map):
        if i % 2:
            block = None
        else:
            block = int(id_number)
            id_number += 1
        blocks.extend([block] * int(block_size))
    return blocks


def last_non_empty_file_block(blocks: list[int | None]) -> dict[str, Any]:
    for i in reversed(range(len(blocks))):
        if blocks[i] is not None:
            return {"position": i, "block_value": blocks[i]}
    raise ValueError("All blocks are empty.")


def first_empty_file_block_position(blocks: list[int | None]) -> int:
    for i in range(len(blocks)):
        if blocks[i] is None:
            return i
    raise ValueError("All blocks are non-empty.")


def is_compacted(blocks: list[int | None]) -> bool:
    first_none_position = first_empty_file_block_position(blocks)
    return all(block is None for block in blocks[first_none_position:])


def compactify(blocks: list[int | None]) -> list[int | None]:
    blocks = blocks.copy()
    while not is_compacted(blocks):
        block_to_move = last_non_empty_file_block(blocks)
        block_to_move_position, block_to_move_value = block_to_move["position"], block_to_move["block_value"]
        blocks[block_to_move_position] = None
        blocks[first_empty_file_block_position(blocks)] = block_to_move_value
    return blocks


def checksum(blocks: list[int | None]) -> int:
    total_checksum = 0
    for i, block in enumerate(blocks):
        if block is not None:
            total_checksum += i * block
    return total_checksum


disk_map_blocks = disk_map_to_blocks(input_txt)
compacted_disk_map_blocks = compactify(disk_map_blocks)
print(checksum(compacted_disk_map_blocks))  # Print: 6332189866718


# Part 2
