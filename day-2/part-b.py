from collections import defaultdict
from functools import reduce
from pathlib import Path


def process_draw(draw, values):
    count, color = draw.split(" ")
    values[color].append(int(count))


def calculate_total(values):
    return reduce(lambda x, y: x * y, (max(dice) for dice in values.values()), 1)


with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

total_sum = 0
for line in lines:
    current_values = defaultdict(list)

    for game in line.split(":")[1].split(";"):
        draws = [draw.strip() for draw in game.strip().split(",")]
        for draw in draws:
            process_draw(draw, current_values)

    total_sum += calculate_total(current_values)

print(total_sum)
