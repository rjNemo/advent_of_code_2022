from common.file import read_data

test_cases = [
    {"input": "mjqjpqmgbljsphdztnvjfqwrcgsmlb", "packet": 7, "message": 19},
    {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "packet": 5, "message": 23},
    {"input": "nppdvjthqldpwncqszvftbrmjlhg", "packet": 6, "message": 23},
    {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "packet": 10, "message": 29},
    {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "packet": 11, "message": 26},
]


def end_of_start_marker(data: str) -> int:
    return _process_signal(data, 4)


def end_of_message(data: str) -> int:
    return _process_signal(data, 14)


def _process_signal(signal: str, size: int) -> int:
    i = 0
    j = size
    while j < len(signal):
        packet = signal[i:j]
        if len(set(packet)) == len(packet):
            return j

        i += 1
        j += 1

    return 0


if __name__ == "__main__":
    for test in test_cases:
        res = end_of_start_marker(test["input"])
        assert res == test["packet"], f"{res} is not the right value, want {test['packet']}"

    for test in test_cases:
        res = end_of_message(test["input"])
        assert res == test["message"], f"{res} is not the right value, want {test['message']}"

    dataset = read_data()
    print(end_of_start_marker(dataset[0]))
    print(end_of_message(dataset[0]))
