import re


TOTAL_SPACE = 70_000_000
FREE_SPACE_NEEDED = 30_000_000


class Dir:
    def __init__(self, name):
        self.name: str = name
        self.parent: Dir | None = None
        self.children: list[Dir] = []
        self.files: list[File] = []

    def get_size(self) -> int:
        return sum([x.get_size() for x in self.children]) + sum([x.size for x in self.files]) 

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
                curr_dir.files.append(newfile)
            else:
                raise ValueError("Uhhhhhhh, the output is neither a dir or a file???")


def init_tree():
    commands = get_commands("input.txt")
    for command_block in commands[1:]:
        command, output = command_block
        parse_command(command, output)

init_tree()

FREE_SPACE = TOTAL_SPACE - global_dir.get_size()
MIN_DEL_SIZE = FREE_SPACE_NEEDED - FREE_SPACE

dir_size = None
def solve(node):
    global dir_size
    node_size = node.get_size()
    if (node_size >= MIN_DEL_SIZE and (dir_size is None or node_size < dir_size)):
        dir_size = node_size
    for c in node.children:
        solve(c)

solve(global_dir)
print(dir_size)

