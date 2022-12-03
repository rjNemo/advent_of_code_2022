from string import ascii_letters

test_dataset = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def priority_shared_items_sum_1(data: list[str]) -> int:
    return sum(process(line) for line in data)


def process(rucksack: str) -> int:
    size = len(rucksack)
    a = rucksack[: size // 2]
    b = rucksack[size // 2:]
    a = set(a)
    b = set(b)
    item = a.intersection(b)
    return ascii_letters.index(item.pop()) + 1


def read_data() -> list[str]:
    with open("./input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def priority_shared_items_sum_2(data: list[str]) -> int:
    badges = []
    i = 0
    while i < len(data):
        group = [set(line) for line in data[i: i + 3]]
        badge = find_intersection(group)
        badges.append(ascii_letters.index(badge) + 1)
        i += 3
    return sum(badges)


def find_intersection(group: list[set[str]]) -> str:
    return group[0].intersection(group[1]).intersection(group[2]).pop()


if __name__ == "__main__":
    dataset = read_data()

    res = priority_shared_items_sum_1(dataset)
    assert res == 157, f"{res} is not the right value"

    res = priority_shared_items_sum_2(dataset)
    assert res == 70, f"{res} is not the right value"
