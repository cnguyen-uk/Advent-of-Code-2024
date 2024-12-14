"""
Day 4: Ceres Search
https://adventofcode.com/2024/day/4
"""

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
def row_count(word_to_match: str, word_search: list[str]) -> int:
    adjacent_letters = len(word_to_match)
    count = 0
    for m in range(len(word_search)):
        for n in range(len(word_search[m]) - adjacent_letters + 1):
            word = ""
            for o in range(adjacent_letters):
                word += word_search[m][n + o]
            if word == word_to_match:
                count += 1
    return count


def column_count(word_to_match: str, word_search: list[str]) -> int:
    adjacent_letters = len(word_to_match)
    count = 0
    for m in range(len(word_search[0])):
        for n in range(len(word_search) - adjacent_letters + 1):
            word = ""
            for o in range(adjacent_letters):
                word += word_search[n + o][m]
            if word == word_to_match:
                count += 1
    return count


def leading_diagonal_count(word_to_match: str, word_search: list[str]) -> int:
    adjacent_letters = len(word_to_match)
    count = 0
    for m in range(len(word_search) - adjacent_letters + 1):
        for n in range(len(word_search) - adjacent_letters + 1):
            word = ""
            for o in range(adjacent_letters):
                word += word_search[m + o][n + o]
            if word == word_to_match:
                count += 1
    return count


def off_diagonal_count(word_to_match: str, word_search: list[str]) -> int:
    adjacent_letters = len(word_to_match)
    count = 0
    for m in range(len(word_search) - adjacent_letters + 1):
        for n in range(len(word_search) - 1, adjacent_letters - 1 - 1, -1):
            word = ""
            for o in range(adjacent_letters):
                word += word_search[m + o][n - o]
            if word == word_to_match:
                count += 1
    return count


def word_search_count(word_to_search: str, word_search: list[str]) -> int:
    return sum(
        [
            row_count(word_to_match=word_to_search, word_search=word_search),
            column_count(word_to_match=word_to_search, word_search=word_search),
            leading_diagonal_count(word_to_match=word_to_search, word_search=word_search),
            off_diagonal_count(word_to_match=word_to_search, word_search=word_search),
        ]
    )


print(sum([word_search_count(word_to_search=word, word_search=input_list) for word in ["XMAS", "SAMX"]]))  # Print: 2517


# Part 2
def word_appears_in_x_shape(
    word_search: list[str], centre_position: tuple[int, int], centre_letter: str, ordered_surrounding_letters: str
) -> bool:
    """Check if a four-letter word is in an X-shape, in a given surrounding order, starting clockwise from top-left."""
    top_left, top_right, bottom_left, bottom_right = tuple(ordered_surrounding_letters)
    i, j = centre_position
    return (
        word_search[i][j] == centre_letter
        and word_search[i - 1][j - 1] == top_left
        and word_search[i - 1][j + 1] == top_right
        and word_search[i + 1][j - 1] == bottom_left
        and word_search[i + 1][j + 1] == bottom_right
    )


def count_mas_x_shapes(word_search: list[str]) -> int:
    n = len(word_search)
    count = 0

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (
                word_appears_in_x_shape(
                    word_search=word_search,
                    centre_position=(i, j),
                    centre_letter="A",
                    ordered_surrounding_letters="MSMS",
                )
                or word_appears_in_x_shape(
                    word_search=word_search,
                    centre_position=(i, j),
                    centre_letter="A",
                    ordered_surrounding_letters="MMSS",
                )
                or word_appears_in_x_shape(
                    word_search=word_search,
                    centre_position=(i, j),
                    centre_letter="A",
                    ordered_surrounding_letters="SSMM",
                )
                or word_appears_in_x_shape(
                    word_search=word_search,
                    centre_position=(i, j),
                    centre_letter="A",
                    ordered_surrounding_letters="SMSM",
                )
            ):
                count += 1

    return count


print(count_mas_x_shapes(word_search=input_list))  # Print: 1960
