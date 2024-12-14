"""
Day 5: Print Queue
https://adventofcode.com/2024/day/5
"""

from typing import TypedDict, cast

with open("input.txt") as input_txt:
    input_list = input_txt.read().splitlines()


# Part 1
class PageInformation(TypedDict):
    rules: list[str]
    queues: list[list[str]]


def extract_rules_and_queues(pages_information: list[str]) -> PageInformation:
    rules = []
    queues = []
    for row in pages_information:
        if "|" in row:
            rules.append(row)
        elif "," in row:
            queues.append(row.split(","))
    return {"rules": rules, "queues": queues}


def satisfies_rules(queue: list[str], rules_list: list[str]) -> dict[str, bool | str]:
    relevant_rules = [rule for rule in rules_list if set(rule.split("|")).issubset(queue)]
    for page in queue:
        for rule in relevant_rules:
            if page in rule:
                first_page = rule.split("|")[0]
                if page != first_page:
                    return {"passed": False, "failed_rule": rule}
        relevant_rules = [rule for rule in relevant_rules if page not in rule]
    return {"passed": True}


def correctly_ordered_pages(pages_information: list[str]) -> list[list[str]]:
    rules_and_queues = extract_rules_and_queues(pages_information=pages_information)
    rules, queues = rules_and_queues["rules"], rules_and_queues["queues"]
    return [queue for queue in queues if satisfies_rules(queue=queue, rules_list=rules)["passed"]]


def middle_pages(pages: list[list[str]]) -> list[int]:
    return [int(page[int(len(page) / 2)]) for page in pages]


correct_pages = correctly_ordered_pages(pages_information=input_list)
print(sum(middle_pages(pages=correct_pages)))  # Print: 4959


# Part 2
def fix_pages(queue: list[str], rules_list: list[str]) -> list[str]:
    while True:
        result = satisfies_rules(queue, rules_list)
        if not result["passed"]:
            failed_rule = cast(str, result["failed_rule"])
            failed_page_1, failed_page_2 = failed_rule.split("|")[0], failed_rule.split("|")[1]
            page_1, page_2 = queue.index(failed_page_1), queue.index(failed_page_2)
            queue[page_1], queue[page_2] = queue[page_2], queue[page_1]
        else:
            break
    return queue


def fixed_incorrectly_ordered_pages(pages_information: list[str]) -> list[list[str]]:
    rules_and_queues = extract_rules_and_queues(pages_information=pages_information)
    rules, queues = rules_and_queues["rules"], rules_and_queues["queues"]
    return [
        fix_pages(queue=queue, rules_list=rules)
        for queue in queues
        if not satisfies_rules(queue=queue, rules_list=rules)["passed"]
    ]


fixed_pages = fixed_incorrectly_ordered_pages(pages_information=input_list)
print(sum(middle_pages(pages=fixed_pages)))  # Print: 4655
