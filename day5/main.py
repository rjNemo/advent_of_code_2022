from dataclasses import dataclass

from common.file import read_data

test_dataset = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


@dataclass(frozen=True)
class Move:
    quantity: int
    of: int
    to: int


def top_crates_1(data: list) -> str:
    stacks, instructions = process_data(data)
    stacks = find_top_crates_1(stacks, instructions)
    return output_top_crates(stacks)


def find_top_crates_1(stacks: list[list[str]], instructions: list[Move]) -> list[list[str]]:
    for step in instructions:
        for _ in range(step.quantity):
            stacks[step.to].append(stacks[step.of].pop())

    return stacks


def find_top_crates_2(stacks: list[list[str]], instructions: list[Move]) -> list[list[str]]:
    for step in instructions:
        tmp = []
        print(tmp)
        for _ in range(step.quantity):
            tmp.insert(0, stacks[step.of].pop())
            print(tmp)
        stacks[step.to].extend(tmp)

    return stacks


def top_crates_2(data: list[str]) -> str:
    stacks, instructions = process_data(data)
    stacks = find_top_crates_2(stacks, instructions)
    return output_top_crates(stacks)


def process_data(data: list[str]) -> tuple[list[list[str]], list[Move]]:
    rows = []
    steps = []
    for line in data:
        if line == "" or line.strip()[0] == "1":
            continue
        if line[0] == "m":
            steps.append(line)
        else:
            rows.append(line)

    stacks = _build_stacks(rows)
    instructions = _build_instructions(steps)

    return stacks, instructions


def _build_stacks(rows: list[str]) -> list[list[str]]:
    stacks = []
    i = 0
    while i < len(rows[0]):
        stack = []
        for row in rows:
            crate = row[i + 1 : i + 2]
            if crate.strip() != "":
                stack.insert(0, crate)

        i += 4
        stacks.append(stack)
    return stacks


def _build_instructions(instructions: list[str]) -> list[Move]:
    moves = []
    for step in instructions:
        splits = step.split(" ")
        qty = int(splits[1])
        of = int(splits[3]) - 1
        to = int(splits[5]) - 1
        moves.append(Move(quantity=qty, of=of, to=to))

    return moves


def output_top_crates(stacks) -> str:
    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    dataset = read_data()

    res = top_crates_1(dataset)
    assert res == "CMZ", f"{res} is not the right value"

    res = top_crates_2(dataset)
    assert res == "MCD", f"{res} is not the right value"
