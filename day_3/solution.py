def get_rucksacks(filename):
    with open(filename, "r") as f:
        file = f.read()
        return file.strip("\n").split("\n")

def calc_priority(char):
    if ord("a") <= ord(char) <= ord("z"):
        return ord(char) - ord("a") + 1

    elif ord("A") <= ord(char) <= ord("Z"):
        return ord(char) - ord("A") + calc_priority("z") + 1

    else:
        return 0

def get_unique(rucksack):
    hlf = len(rucksack) // 2

    set_a, set_b = set(), set()
    for i, letter in enumerate(rucksack):
        if i < hlf:
            set_a.add(letter)
        else:
            set_b.add(letter)

        if letter in set_a and letter in set_b:
            return letter
    raise ValueError("No common letter in rucksacks")


total = 0
for rucksack in get_rucksacks("input.txt"):
    unique = get_unique(rucksack)
    priority = calc_priority(unique)
    total += priority

print(total)
