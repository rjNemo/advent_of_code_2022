from dataclasses import dataclass, field
from typing import Self

from common.file import read_data

DIRECTORY = "directory"
FILE = "file"
TOTAL_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000

test_data = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


@dataclass
class Node:
    node_type: str
    name: str
    _size: int = 0
    children: list[Self] = field(default_factory=list)
    parent: Self | None = None

    def add(self, leaf: Self):
        leaf.parent = self
        self.children.append(leaf)

    @property
    def size(self) -> int:
        if self.node_type == DIRECTORY:
            self.size = sum(child.size for child in self.children)
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value


def new_leaf(command: str) -> Node:
    a, b = command.split(" ")

    if a == "dir":
        node_type = DIRECTORY
        name = b
        size = 0
    else:
        node_type = FILE
        name = b
        size = int(a)

    node = Node(node_type=node_type, name=name)
    node.size = size
    return node


def move_to(tree: Node, directory: str) -> Node:
    if directory == "..":
        return tree.parent
    return [node for node in tree.children if node.name == directory][0]


def build_tree(data: list[str]) -> list[Node]:
    root = Node(node_type=DIRECTORY, name="/")
    current = root

    directories = [root]

    i = 1
    while i < len(data[1:]):
        if "$ cd" in data[i]:
            _, _, directory = data[i].split(" ")
            current = move_to(current, directory)
            i += 1
        if "$ ls" in data[i]:
            i += 1
            while i <= len(data[1:]) and data[i][0] != "$":
                leaf = new_leaf(data[i])
                if leaf.node_type == DIRECTORY:
                    directories.append(leaf)
                current.add(leaf)
                i += 1
    return directories


def total_files_size(data: list[str]) -> int:
    dirs = build_tree(data)
    return sum(directory.size for directory in dirs if directory.size < 100_000)


def smallest_directory_to_delete(data: list[str]) -> int:
    dirs = build_tree(data)
    dirs.sort(key=lambda x: x.size)
    return [d.size for d in dirs if (TOTAL_SPACE - dirs[-1].size + d.size) > UPDATE_SIZE][0]


if __name__ == "__main__":
    dataset = read_data()

    res = total_files_size(test_data)
    assert res == 95437, f"{res} is not the right value, want 95437"

    print(f"Part 1 solution: {total_files_size(dataset)}")

    res = smallest_directory_to_delete(test_data)
    assert res == 24933642, f"{res} is not the right value, want 24933642"

    print(f"Part 2 solution: {smallest_directory_to_delete(dataset)}")
