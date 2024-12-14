"""
Day 13: Claw Contraption
https://adventofcode.com/2024/day/13
"""

import re

import numpy as np
from numpy.typing import NDArray

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
def button_and_prize_data_to_arrays(input_data: list[str]) -> dict[str, list[int]]:
    def extract_int(data: str, pattern: str) -> int:
        match = re.search(pattern, data)
        if match:
            return int(match.group(1))
        raise ValueError(f"No match found for pattern: {pattern}")

    button_a_data, button_b_data, prize_data = "", "", ""
    for line in input_data:
        if "Button A" in line:
            button_a_data = line.replace("Button A: ", "")
        if "Button B" in line:
            button_b_data = line.replace("Button B: ", "")
        if "Prize" in line:
            prize_data = line.replace("Prize: ", "")
    x_array = [extract_int(button_a_data, r"X\+(\d+)"), extract_int(button_b_data, r"X\+(\d+)")]
    y_array = [extract_int(button_a_data, r"Y\+(\d+)"), extract_int(button_b_data, r"Y\+(\d+)")]
    answer_array = [extract_int(prize_data, r"X=(\d+)"), extract_int(prize_data, r"Y=(\d+)")]
    return {
        "equation_1": x_array,
        "equation_2": y_array,
        "answer": answer_array,
    }


def input_data_to_arrays(input_data: list[str]) -> list[dict[str, list[int]]]:
    equation_data = []
    for i in range(0, len(input_data), 4):
        input_data_chunk = input_data[i : i + 3]
        equation_data.append(button_and_prize_data_to_arrays(input_data_chunk))
    return equation_data


def solve_linear_equation(
    equation_1: list[int], equation_2: list[int], answer: list[int], integer_solutions_only: bool
) -> NDArray[np.int64]:
    equation_arrays = np.array([equation_1, equation_2])
    answer_array = np.array(answer)
    solution = np.linalg.solve(equation_arrays, answer_array)
    if integer_solutions_only:
        solution = solution.round().astype(int)
    is_solution_correct = np.allclose(np.dot(equation_arrays, solution), answer_array, rtol=1.0e-100)
    if is_solution_correct:
        return solution
    return np.array([])


def solve_input_data(
    input_data: list[str], integer_solutions_only: bool, add_10000000000000: bool
) -> list[NDArray[np.int64]]:
    solutions = []
    equation_data = input_data_to_arrays(input_data)
    for equation_set in equation_data:
        equation_1 = equation_set["equation_1"]
        equation_2 = equation_set["equation_2"]
        answer = equation_set["answer"]
        if add_10000000000000:
            answer = [answer + 10000000000000 for answer in answer]
        solution = solve_linear_equation(
            equation_1=equation_1, equation_2=equation_2, answer=answer, integer_solutions_only=integer_solutions_only
        )
        solutions.append(solution)
    return solutions


def all_prize_cost(input_data: list[str], add_10000000000000: bool = False) -> int:
    solutions = solve_input_data(
        input_data=input_data, integer_solutions_only=True, add_10000000000000=add_10000000000000
    )
    solutions = [solution for solution in solutions if solution.size != 0]  # Filter out np.array([])
    cost = 0
    for solution in solutions:
        cost += solution[0] * 3 + solution[1] * 1
    return cost


print(all_prize_cost(input_data=input_list))  # Print: 31897


# Part 2
print(all_prize_cost(input_data=input_list, add_10000000000000=True))  # Print: 87596249540359
