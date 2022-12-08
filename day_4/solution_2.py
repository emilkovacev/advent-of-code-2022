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

# a, c, b, d  a <= c <= b
# c, a, d, b  a <= d <= b

def has_subset(a, b, c, d):
    return a <= c <= b or a <= d <= b or \
           c <= a <= d or c <= b <= d


total = 0
for pair in parse_file("input.txt"):
    if has_subset(*pair):
        total += 1

print(f"subsets: {total}")
