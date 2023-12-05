from pathlib import Path

THRESHOLD = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def process_draw(draw):
    count, color = draw.split(" ")
    return int(count) <= THRESHOLD[color]


with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

total = sum(
    game_id
    for game_id, line in enumerate(lines, start=1)
    if all(
        process_draw(draw.strip())
        for game in line.split(":")[1].split(";")
        for draw in game.strip().split(",")
    )
)

print(total)
