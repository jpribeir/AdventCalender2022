# Day 5 of the 2022 Advent of Code
import re

# Read input file
#with open("../include/example5.inc","r") as cargo_file:
with open("../include/input5.inc","r") as cargo_file:
    cargo_list = cargo_file.readlines()

num_stacks = int(len(cargo_list[0])/4)
cargo_stack = [ "" ] * num_stacks
move_list = []
for line in cargo_list:
    if line.startswith("move"): move_list.append(line.strip())
    elif "[" in line:
        j = 0
        for i in range(1,len(line),4):
            if line[i] != " ": cargo_stack[j]+=line[i]
            j += 1

for move in move_list:
    num_crates = int(move.split("move ")[1][0])
    orig_stack = int(move.split("from ")[1][0])-1
    dest_stack = int(move.split("to ")[1][0])-1
    moving_crates = cargo_stack[orig_stack][0:num_crates]
    cargo_stack[orig_stack] = cargo_stack[orig_stack][num_crates:]
    cargo_stack[dest_stack] = moving_crates[::-1]+cargo_stack[dest_stack]

print(cargo_stack)