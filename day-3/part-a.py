from pathlib import Path

with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

CHARS = [list(line) for line in lines]
ROWS = len(CHARS)
COLS = len(CHARS[0])


def process_row(row):
    total = 0
    n, part = 0, False
    for col in range(COLS + 1):
        if col < COLS and CHARS[row][col].isdigit():
            n = n * 10 + int(CHARS[row][col])
            part |= any(
                CHARS[r][c] not in ".1234567890"
                for r in range(row - 1, row + 2)
                for c in range(col - 1, col + 2)
                if 0 <= r < ROWS and 0 <= c < COLS
            )

        elif n > 0:
            if part:
                total += n
            n, part = 0, False

    return total


print(sum(process_row(row) for row in range(ROWS)))
