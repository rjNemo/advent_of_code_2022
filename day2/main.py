from typing import Generator


def total_score(data: Generator[list[str]]):
    points = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    score = 0
    for row in data:
        a, b = row
        res = (points[a] - points[b]) % 3
        if res == 0:
            # it's a draw
            score += 3 + points[b]
        elif res == 2:
            # won
            score += 6 + points[b]
        else:
            # lose
            score += points[b]
    return score


def read_data() -> Generator[list[str]]:
    with open("./input.txt", "r") as f:
        return (row.strip().split(" ") for row in f.readlines())


if __name__ == "__main__":
    test_data = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z"),
    ]
    data = read_data()
    print(total_score(data))
