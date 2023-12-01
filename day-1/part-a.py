from pathlib import Path

with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

total = 0
for line in lines:
    digits = list(filter(str.isdigit, line))
    total += int(f"{digits[0]}{digits[-1]}")

print(total)
