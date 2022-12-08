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

def get_unique(rucksacks):
    assert len(rucksacks) == 3
    rucksack_setup = [set(), set(), set()]
    for i, rucksack in enumerate(rucksacks):
        for letter in rucksack:
            if letter in rucksack_setup[i-1] and letter in rucksack_setup[i-2]:
                return letter
            rucksack_setup[i].add(letter)
    raise ValueError("No common letter in rucksacks")


total = 0
rucksacks = get_rucksacks("test_input.txt")
for i in range(0, len(rucksacks), 3):
    group_rucksacks = rucksacks[i:i+3]

    print(group_rucksacks)
    unique = get_unique(group_rucksacks)
    priority = calc_priority(unique)
    total += priority

print(total)
