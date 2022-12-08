n_unique = 14

def solution(filename):
    with open(filename, "r") as f:
        code = f.readline()
        for i in range(len(code) - n_unique - 1):
            signal = code[i:i+n_unique]
            if len(set(signal)) == n_unique:
                return i + n_unique
        return -1

signal = solution("input.txt")
print(f"Solution: {signal}")
