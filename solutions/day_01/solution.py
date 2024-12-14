"""
Day 1: Historian Hysteria
https://adventofcode.com/2024/day/1
"""

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()

left_list = []
right_list = []
for row in input_list:
    first, second = row.split("   ")
    left_list.append(int(first))
    right_list.append(int(second))


# Part 1
left_list.sort()
right_list.sort()
combined_list = zip(left_list, right_list)
total_distance = sum([abs(i - j) for i, j in combined_list])
print(total_distance)  # Print: 1110981


# Part 2
appearance_counter = {}
for i in left_list:
    if i not in appearance_counter:
        appearance_counter[i] = 0
    appearance_count = right_list.count(i)
    appearance_counter[i] += appearance_count

total_sum = 0
for k, v in appearance_counter.items():
    total_sum += k * v
print(total_sum)  # Print: 24869388
