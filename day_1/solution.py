import re

with open("input.txt", "r") as f:
    file = f.read()
    calories = []
    for cals in re.split(r"\n\n", file):
        total = 0
        for i in cals.strip('\n').split("\n"):
            total += int(i)

        calories.append(total)

    calories.sort(reverse=True)
    print(sum(calories[:3]))
