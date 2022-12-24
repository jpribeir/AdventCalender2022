# Day 23 of the 2022 Advent of Code

def expandMatrix():
    return elfs_matrix

# Read input file
with open("../include/example23.inc","r") as elfs_file:
#with open("../include/input23.inc","r") as elfs_file:
    elfs_matrix = list(map(lambda a: a.strip().split(","),elfs_file.readlines()))

print(elfs_matrix)

#print("Part1: %s"%total_area)
#print("Part2: %s"%empty_count)