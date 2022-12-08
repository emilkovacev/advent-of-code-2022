import re


MAX_SIZE = 100_000


class Dir:
    def __init__(self, name):
        self.name: str = name
        self.parent: Dir | None = None
        self.children: list[Dir | File] = []

    def get_size(self) -> int:
        return sum([x.get_size() for x in self.children if x is not None])

    def __str__(self) -> str:
        return f"{self.name} : {self.get_size()}"

class File:
    def __init__(self, name, size):
        self.name: str = name
        self.size: int = size

    def get_size(self) -> int:
        return self.size

    def __str__(self):
        return f"{self.name} : {self.size}"


curr_dir = global_dir = Dir("/")


# for input:
#   $ cd /
#   $ ls
#   dir dpbwg
#   dir dvwfscw
#
# this function will output:
#   [
#       ("cd /", []),
#       ("ls", ["dir dpbwg", "dir dvwfscw"]),
#   ]

def get_commands(filename):
    with open(filename, "r") as f:
        file = f.read()

        retval = []
        for block in re.findall(r"(\$\s[^\n]+)([^$]+)", file):
            command, output = block
            output = output.strip("\n").split("\n")
            retval.append((command, output))
        return retval


def parse_command(command, output):
    global curr_dir

    is_cd = re.match(r"\$ cd (.+)", command)
    is_ls = re.match(r"\$ ls", command)

    if is_cd and is_cd.group(1) == "..":
        if curr_dir.parent is None:
            raise ValueError("current dir should have a parent!!!")
        curr_dir = curr_dir.parent
    elif is_cd:
        child_dir = Dir(is_cd.group(1))
        curr_dir.children.append(child_dir)
        child_dir.parent = curr_dir
        curr_dir = child_dir

    elif is_ls:
        dir_re = re.compile(r"dir\s(.+)")
        file_re = re.compile(r"(\d+)\s(.+)")
        for out in output:
            is_dir = dir_re.match(out)
            is_file = file_re.match(out)
            if is_dir:
                pass
                
            elif is_file:
                size, filename = is_file.group(1, 2)
                newfile = File(filename, int(size))
                curr_dir.children.append(newfile)
            else:
                raise ValueError("Uhhhhhhh, the output is neither a dir or a file???")


total = 0

def get_total(node):
    if type(node) == Dir:
        total = 0
        if node.get_size() <= MAX_SIZE:
            total += node.get_size()

        total += sum([get_total(x) for x in node.children])
        return total

    else:
        return 0
    

commands = get_commands("input.txt")
for command_block in commands[1:]:
    command, output = command_block
    # print(command)
    parse_command(command, output)
    # print(curr_dir)

print(get_total(global_dir))
# print_filetree(global_dir)

