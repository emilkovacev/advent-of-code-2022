from enum import Enum

WIN_PTS = 6
TIE_PTS = 3
LOSE_PTS = 0

class Move(Enum):
    Rock = A = 1
    Paper = B = 2
    Scissor = C = 3

class Outcome(Enum):
    Win = Z = "Z"
    Tie = Y = "Y"
    Lose = X = "X"

winner = {
    Move.Scissor: Move.Rock,
    Move.Rock: Move.Paper,
    Move.Paper: Move.Scissor 
}

def get_guide(filename):
    with open(filename, "r") as f:
        file = f.read()
        return [x.split(" ") for x in file.strip("\n").split("\n")]

def score(move_a, move_b):
    score = 0

    if winner[move_a] == move_b:
        score = WIN_PTS
    elif move_a == move_b:
        score = TIE_PTS
    else:
        score = LOSE_PTS

    score += move_b.value  # add value of move
    return score

def calc_move(move, outcome):
    move = Move[move]
    outcome = Outcome[outcome]

    if outcome == Outcome.Win:
        retval = winner[move]   
    elif outcome == Outcome.Tie:
        retval = move
    else:
        retval = winner[winner[move]] # Loser is the winner of the winner

    return (move, retval)

total = 0
guide = get_guide("input.txt")
for move_a, outcome in guide:
    move_a, move_b = calc_move(move_a, outcome)
    curr_score = score(move_a, move_b)
    total += curr_score

print(f"part 2: {total}")

