def max_calories() -> int:
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


if __name__ == "__main__":
    print(max_calories())
