# Day 7 of the 2022 Advent of Code
# Class to instantiate directories, detailing its parent directory and child directories/files
class Dir():
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.children_dict = {}
        self.files_dict = {}
        self.total_size = 0
    
    def addChild(self,child):
        self.children_dict[child] = Dir(child,self)
    
    def addFile(self,file,size):
        self.files_dict[file] = size
        self.total_size += int(size)

# Go through directory tree recursively updating variable when finding a new lower eligible value
def goInto(dir,delfolder_size):
    if dir.total_size < delfolder_size and dir.total_size >= minsize_to_delete: delfolder_size = dir.total_size
    for child in dir.children_dict.values(): delfolder_size = goInto(child,delfolder_size)
    return delfolder_size

# Read input file
with open("../include/input7.inc","r") as cmd_file:
    cmd_list = list(map(lambda a: a.strip(),cmd_file.readlines()))

root = Dir("/","/")
current_node = root
sizecap = 100000
total_sum = 0
for cmd in cmd_list[1:]:
    if cmd.startswith("$ cd"):
        if cmd.split()[-1] == "..":
            if current_node.total_size<=sizecap: total_sum += current_node.total_size
            (current_node.parent).total_size += current_node.total_size
            current_node = current_node.parent
        else: current_node = current_node.children_dict[cmd.split()[2]]
    elif not cmd.startswith("$"):
        if cmd.startswith("dir"): current_node.addChild(cmd.split()[1])
        else: current_node.addFile(cmd.split()[1],cmd.split()[0])

# Finish up the size count for outermost directories (since the input doesn't "cd.." the last directories)
while current_node.name!="/":
    if current_node.total_size <=sizecap: total_sum += current_node.total_size
    (current_node.parent).total_size += current_node.total_size
    current_node = current_node.parent

# Recursively find the lowest size directory bigger than minsize_to_delete in the tree
total_space = 70000000
needed_free_space = 30000000
minsize_to_delete = needed_free_space - (total_space - root.total_size)
delfolder_size = goInto(root,needed_free_space)

print("Part1: %s"%total_sum)
print("Part2: %s"%delfolder_size)