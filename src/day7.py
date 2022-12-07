# Day 7 of the 2022 Advent of Code
# Class to instantiate directories, detailing its parent directory and child directories/files
class Dir():
    # Initiate the object
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

# Read input file
#with open("../include/input7.inc","r") as cmd_file:
with open("../include/example7.inc","r") as cmd_file:
    cmd_list = list(map(lambda a: a.strip(),cmd_file.readlines()))

root = Dir("/","/")
current_node = root
sizecap = 100000
total_sum = 0
minsize_to_delete = 30000000
delfolder_size = 70000000
for cmd in cmd_list[1:]:
    #print("### %s"%cmd)
    if cmd.startswith("$ cd"):
        if cmd.split()[-1] == "..":
            if current_node.total_size<=sizecap: total_sum += current_node.total_size
            (current_node.parent).total_size += current_node.total_size
            current_node = current_node.parent
        else: current_node = current_node.children_dict[cmd.split()[2]]
    elif not cmd.startswith("$"):
        if cmd.startswith("dir"): current_node.addChild(cmd.split()[1])
        else: current_node.addFile(cmd.split()[1],cmd.split()[0])
    #print("%s -> %s"%(current_node.name,current_node.total_size))

# Finish up the size count for outermost directories
while current_node.name!="/":
    if current_node.total_size <=sizecap: total_sum += current_node.total_size
    if current_node.total_size<delfolder_size and current_node.total_size>=minsize_to_delete: delfolder_size = current_node.total_size
    (current_node.parent).total_size += current_node.total_size
    current_node = current_node.parent
minsize_to_delete = 30000000 - (70000000 - root.total_size)
#NOW PART2: search tree for smallest folder that's bigger than minsize_to_delete

print("Part1: %s"%total_sum)
#print("Part2: %s"%delfolder_size)