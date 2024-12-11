"""
Day 7: Bridge Repair
https://adventofcode.com/2024/day/7
"""

import itertools

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
def generate_equations(operands: list[int], operators: list[str]) -> list[str]:
    equations = []
    operator_count = len(operands) - 1
    for operator_combination in itertools.product(operators, repeat=operator_count):
        equation_parts = []
        for i, operand in enumerate(operands):
            equation_parts.append(str(operand))
            if i < len(operator_combination):
                equation_parts.append(operator_combination[i])
        equation = " ".join(map(str, equation_parts))
        equations.append(equation)
    return equations


def evaluate_let_to_right(equation: str) -> int:
    equation_parts = equation.split(" ")
    equation_result = int(equation_parts[0])
    for i in range(1, len(equation_parts), 2):
        operator = equation_parts[i]
        operand = int(equation_parts[i + 1])
        if operator == "+":
            equation_result += operand
        elif operator == "*":
            equation_result *= operand
        elif operator == "||":
            equation_result = int(str(equation_result) + str(operand))
    return equation_result


def is_equation_possible(target_result: int, operands: list[int], operators: list[str]) -> bool:
    candidate_equations = generate_equations(operands=operands, operators=operators)
    for equation in candidate_equations:
        equation_result = evaluate_let_to_right(equation)
        if equation_result == target_result:
            return True
    return False


def sum_possible_equations(input_equations: list[str], operators: list[str]) -> int:
    result_total = 0
    for line in input_equations:
        result, numbers = int(line.split(": ")[0]), [int(num) for num in line.split(": ")[1].split(" ")]
        if is_equation_possible(target_result=result, operands=numbers, operators=operators):
            result_total += result
    return result_total


print(sum_possible_equations(input_equations=input_list, operators=["+", "*"]))  # Print: 1260333054159


# Part 2
print(sum_possible_equations(input_equations=input_list, operators=["+", "*", "||"]))  # Print: 162042343638683
