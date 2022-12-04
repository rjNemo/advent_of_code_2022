from typing import Callable, Iterable

from common.file import read_data

test_dataset = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def find_overlapping_assignments_1(data: list[str]) -> int:
    return sum(process(line, all) for line in data)


def find_overlapping_assignments_2(data: list[str]) -> int:
    return sum(process(line, any) for line in data)


def process(line: str, func: Callable[[Iterable], bool]) -> int:
    a, b = line.strip().split(",")

    start_a, end_a = [int(x) for x in a.split("-")]
    int_a = range(start_a, end_a + 1)
    start_b, end_b = [int(x) for x in b.split("-")]
    int_b = range(start_b, end_b + 1)

    return int(func(x in int_b for x in int_a) or func(x in int_a for x in int_b))


if __name__ == "__main__":
    dataset = read_data()

    res = find_overlapping_assignments_1(dataset)
    assert res == 2, f"{res} is not the right value"

    res = find_overlapping_assignments_2(dataset)
    assert res == 4, f"{res} is not the right value"
