"""
Day 9: Disk Fragmenter
https://adventofcode.com/2024/day/9
"""

from typing import Any

with open("input.txt") as input_txt:
    input_txt = input_txt.read()


# Part 1
def disk_map_to_blocks(disk_map: str) -> str:
    blocks = ""
    id_number = 0
    for i, block_size in enumerate(disk_map):
        if i % 2:
            block = "."
        else:
            block = str(id_number)
            id_number += 1
        blocks += block * int(block_size)
    return blocks


def last_non_empty_file_block(blocks: str) -> dict[str, Any]:
    for i in reversed(range(len(blocks))):
        if blocks[i] != ".":
            return {"position": i, "block_value": blocks[i]}


def compactify(blocks: str) -> str:
    compacted_blocks = ""
    current_blocks = blocks
    while current_blocks:
        block = current_blocks[0]
        if block != ".":
            compacted_blocks += block
        else:
            block_to_move = last_non_empty_file_block(current_blocks)
            if block_to_move:
                i, block_value = block_to_move["position"], block_to_move["block_value"]
                compacted_blocks += block_value
                current_blocks = current_blocks[:i] + "." + current_blocks[i+1:]
        current_blocks = current_blocks[1:]

    remaining_free_space = len(blocks) - len(compacted_blocks)
    compacted_blocks += "." * remaining_free_space
    return compacted_blocks


def checksum(blocks: str) -> int:
    total_checksum = 0
    for i, block in enumerate(blocks):
        if block != ".":
            total_checksum += i * int(block)
    return total_checksum


disk_map_blocks = disk_map_to_blocks(input_txt)
print(disk_map_blocks)
compacted_disk_map_blocks = compactify(disk_map_blocks)
print(checksum(disk_map_blocks))
print(compacted_disk_map_blocks)
print(checksum(compacted_disk_map_blocks))  # Print: 90489586600


# Part 2
