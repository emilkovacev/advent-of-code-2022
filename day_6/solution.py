def solution(filename):
    with open(filename, "r") as f:
        code = f.readline()
        for i in range(len(code) - 3):
            signal = code[i:i+4]
            if len(set(signal)) == 4:
                return i + 4
        return -1

signal = solution("input.txt")
print(f"Solution: {signal}")
