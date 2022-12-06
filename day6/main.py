from common.file import read_data

test_cases = [
    {"input": "mjqjpqmgbljsphdztnvjfqwrcgsmlb", "expect": 7},
    {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "expect": 5},
    {"input": "nppdvjthqldpwncqszvftbrmjlhg", "expect": 6},
    {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "expect": 10},
    {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "expect": 11},
]


def end_of_start_marker_1(data: str) -> int:
    # use 2 counters
    i = 0
    j = 4
    while j < len(data):
        # read data by window of 4 characters
        packet = data[i:j]
        # check if all are different
        if len(set(packet)) == len(packet):
            # if yes return end counter
            return j

        i += 1
        j += 1

    return 0


if __name__ == "__main__":
    for test in test_cases:
        res = end_of_start_marker_1(test["input"])
        assert res == test["expect"], f"{res} is not the right value, want {test['expect']}"

    dataset = read_data()
    print(end_of_start_marker_1(dataset[0]))
