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
    # iterate over  the data, for each line
    counter = 0
    for line in data:
        # split the ','
        a, b = line.strip().split(",")
        start_a, end_a = [int(x) for x in a.split("-")]
        int_a = range(start_a, end_a + 1)
        start_b, end_b = [int(x) for x in b.split("-")]
        int_b = range(start_b, end_b + 1)
        # if 1 interval in the other increment the counter
        if all(x in int_b for x in int_a) or all(x in int_a for x in int_b):
            counter += 1
    # return the counter
    return counter


if __name__ == "__main__":
    dataset = read_data()

    res = find_overlapping_assignments_1(dataset)
    assert res == 2, f"{res} is not the right value"
    #
    # res = priority_shared_items_sum_2(dataset)
    # assert res == 70, f"{res} is not the right value"
