import re

def parse_file(filename):
    with open(filename, "r") as f:
        file = f.read()
        retval = []
        for line in file.strip("\n").split("\n"):
            print(line)
            m = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line)
            retval.append((
                int(m.group(1)), 
                int(m.group(2)), 
                int(m.group(3)), 
                int(m.group(4))
            ))
        
        return retval

def has_subset(a, b, c, d):
    return a <= c and b >= d or c <= a and d >= b

total = 0
for pair in parse_file("input.txt"):
    if has_subset(*pair):
        total += 1

print(f"subsets: {total}")
