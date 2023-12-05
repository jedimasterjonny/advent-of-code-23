from collections import defaultdict
from pathlib import Path

with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

CHARS = [list(line) for line in lines]
ROWS = len(CHARS)
COLS = len(CHARS[0])
NUMS = defaultdict(list)


def get_search_idx(row, col):
    return {
        (r, c)
        for r in range(row - 1, row + 2)
        for c in range(col - 1, col + 2)
        if 0 <= r < ROWS and 0 <= c < COLS
    }


def process_row(row):
    total = 0
    n, part = 0, False
    gears = set()
    for col in range(COLS + 1):
        if col < COLS and CHARS[row][col].isdigit():
            n = n * 10 + int(CHARS[row][col])
            gears.update(
                [(r, c) for r, c in get_search_idx(row, col) if CHARS[r][c] == "*"],
            )
            part |= any(
                CHARS[r][c] not in ".1234567890" for r, c in get_search_idx(row, col)
            )

        elif n > 0:
            for gear in gears:
                NUMS[gear].append(n)
            if part:
                total += n
            n, part = 0, False
            gears.clear()

    return total


for row in range(ROWS):
    process_row(row)

result = sum(v[0] * v[1] for v in NUMS.values() if len(v) == 2)
print(result)
