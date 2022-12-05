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


def find_top_crates(stacks: list[list[str]], instructions: list[Move]) -> str:
    for step in instructions:
        for _ in range(step.quantity):
            stacks[step.to].append(stacks[step.of].pop())

    return "".join(stack[-1] for stack in stacks)


def top_crates(data: list) -> str:
    stacks, instructions = process_data(data)
    return find_top_crates(stacks, instructions)


if __name__ == "__main__":
    dataset = read_data()

    res = top_crates(dataset)
    assert res == "CMZ", f"{res} is not the right value"
