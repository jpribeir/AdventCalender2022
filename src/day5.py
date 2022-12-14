# Day 5 of the 2022 Advent of Code
# Depending on part the crates are moved in the same order or reversed between stacks
def moveCrates(cargo_stack,move_list,multiple_crates_en):
    for move in move_list:
        num_crates = int((move.split("move ")[1]).split(" from")[0])
        orig_index = int(move.split("from ")[1][0])-1
        dest_index = int(move.split("to ")[1][0])-1
        moving_crates = cargo_stack[orig_index][0:num_crates]
        if multiple_crates_en: cargo_stack[dest_index] = moving_crates+cargo_stack[dest_index]
        else: cargo_stack[dest_index] = moving_crates[::-1]+cargo_stack[dest_index]
        cargo_stack[orig_index] = cargo_stack[orig_index][num_crates:]
    return "".join(list(x[0] for x in cargo_stack))

# Read input file
with open("../include/input5.inc","r") as cargo_file:
    cargo_list = cargo_file.readlines()

# Prepare list of stacks, number of characters in a line is mutiple of the number of stacks
cargo_stack = [ "" ] * int(len(cargo_list[0])/4)
move_list = []
for line in cargo_list:
    if line.startswith("move"): move_list.append(line.strip())
    elif "[" in line:
        j = 0
        for i in range(1,len(line),4):
            if line[i] != " ": cargo_stack[j]+=line[i]
            j += 1

print("Part1: %s"%moveCrates(cargo_stack.copy(),move_list,False))
print("Part2: %s"%moveCrates(cargo_stack.copy(),move_list,True))