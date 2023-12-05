from pathlib import Path

with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

total = 0
for line in lines:
    nums, wins = line.split("|")
    win_vals = set(wins.split())
    num_vals = set(nums.split(":")[1].split())
    interesect_size = len(win_vals & num_vals)
    if interesect_size > 0:
        total += 2 ** (interesect_size - 1)

print(total)
