from pathlib import Path

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with Path("in.txt").open("r") as file:
    lines = [line.rstrip() for line in file]

total = 0

for line in lines:
    digits = []

    for index, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))
        else:
            for int_val, string_val in enumerate(NUMBERS, start=1):
                if line.startswith(string_val, index):
                    digits.append(int_val)

    total += int(f"{digits[0]}{digits[-1]}")

print(total)
