from common.file import read_data


def total_score_1(data: list[list[str]]) -> int:
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


def total_score_2(data: list[list[str]]) -> int:
    points = {
        "A": 0,
        "B": 1,
        "C": 2,
        "X": 1,
        "Y": 0,
        "Z": 2,
    }
    score = 0
    for row in data:
        a, exp = row
        if points[exp] == 0:
            # it's a draw
            score += 3 + points[a] + 1
        elif points[exp] == 2:
            # won
            score += 6 + (points[a] + 1) % 3 + 1
        else:
            # lose
            score += (points[a] - 1) % 3 + 1
    return score


if __name__ == "__main__":
    test_data = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z"),
    ]
    dataset = read_data()
    print(total_score_2(dataset))
