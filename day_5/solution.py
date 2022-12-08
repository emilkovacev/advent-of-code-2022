import re


#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# is translated to
#
# {
#   1: ["Z", "N"],
#   2: ["M", "C", "D"],
#   3: ["P"]
# }

def parse_stacks(stacks):
    retval = {}

    stack_lines = stacks.strip("\n").split("\n")
    for ln in range(len(stack_lines)-1):
        line = stack_lines[ln]
        crates = re.findall(r".(.).\s{0,1}", line)
        for i, match in enumerate(crates):
            if match != ' ':
                retval[i+1] = [match] + retval.get(i+1, [])  # prepend to column stack
       
    return retval


# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
#
# is translated to
#
# [
#   (1, 2, 1),
#   (3, 1, 3),
#   (2, 2, 1),
#   (1, 1, 2)
# ]


def parse_instructions(instructions):
    retval = []

    for line in instructions.strip("\n").split("\n"):
        movement = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        if movement is None:
            raise ValueError("Uhhh, this did not parse correctly lol")

        movement_tuple = tuple(int(x) for x in movement.group(1, 2, 3))
        retval.append(movement_tuple)

    return retval


def get_top_stacks(parsed_instructions):
    retval = ""
    for key in sorted(parsed_instructions):
        stack = parsed_instructions[key]
        retval += stack[-1]

    return retval

def exec_instruction(parsed_instruction, parsed_stack):
    n, from_idx, to_idx = parsed_instruction
    buffer = []
    for _ in range(n):
        crate = parsed_stack[from_idx].pop()
        buffer.append(crate)
    
    parsed_stack[to_idx] = parsed_stack.get(to_idx, []) + buffer

def read_file(filename):
    with open(filename, "r") as f:
        file = f.read()
        stacks, instructions = file.split("\n\n")
        parsed_stacks = parse_stacks(stacks)
        parsed_instructions = parse_instructions(instructions)

        return parsed_stacks, parsed_instructions

def print_stacks(stacks):
    for i in sorted(stacks):
        stack = stacks[i]
        print(f"{i}: {stack}")

def print_instructions(instructions):
    for ins in instructions:
        print(ins)

stacks, instructions = read_file("input.txt")
for i in instructions:
    exec_instruction(i, stacks)

top_stacks = get_top_stacks(stacks)
print_stacks(stacks)

print(f"Top stacks: {top_stacks}")
