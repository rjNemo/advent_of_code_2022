def max_calories_1() -> int:
    with open("./input.txt", "r") as f:
        calories = 0
        tmp = 0
        for line in f.readlines():
            if (c := line.strip()) != "":
                tmp += int(c)
            else:
                calories = max(calories, tmp)
                tmp = 0
    return calories


def max_calories_2() -> int:
    with open("./input.txt", "r") as f:
        calories = []
        tmp = 0
        for line in f.readlines():
            if (c := line.strip()) != "":
                tmp += int(c)
            else:
                calories.append(tmp)
                calories.sort(reverse=True)
                calories = calories[:3]
                tmp = 0
    return sum(calories)


if __name__ == "__main__":
    print(max_calories_2())
