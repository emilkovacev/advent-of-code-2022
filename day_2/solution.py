from enum import Enum

WIN_PTS = 6
TIE_PTS = 3
LOSE_PTS = 0

class Move(Enum):
    Rock = A = X = 1
    Paper = B = Y = 2
    Scissor = C = Z = 3

winner = {
    Move.Rock: Move.Scissor,
    Move.Paper: Move.Rock,
    Move.Scissor: Move.Paper
}

def get_guide(filename):
    with open(filename, "r") as f:
        file = f.read()
        return [x.split(" ") for x in file.strip("\n").split("\n")]

def score(a, b):
    score = 0
    move_a, move_b = Move[a], Move[b]

    if winner[move_b] == move_a:
        score = WIN_PTS
    elif move_a == move_b:
        score = TIE_PTS
    else:
        score = LOSE_PTS

    score += move_b.value  # add value of move
    return score

def part_1():
    total = 0
    guide = get_guide("input.txt")
    for moveset in guide:
        print(moveset)
        total += score(*moveset)

    print(f"part 1: {total}")

part_1()
