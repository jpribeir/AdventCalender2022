# Day 10 of the 2022 Advent of Code
def validList(num):
    return list(range(num,num+3))

# Read input file
with open("../include/input10.inc","r") as cycle_file:
    cycle_list = list(map(lambda a: a.strip(),cycle_file.readlines()))

interesting_dict = {20:0,
                    60:0,
                    100:0,
                    140:0,
                    180:0,
                    220:0}
X = 1
screen_matrix = ["."*40]*6
valid_list = validList(0)
cycle_count = 0
for line in cycle_list:
    # Print "@" if pixel is one of 3 valid indexes
    if int(cycle_count%40) in valid_list: screen_matrix[int(cycle_count/40)] = screen_matrix[int(cycle_count/40)][0:(cycle_count%40)]+"@"+screen_matrix[int(cycle_count/40)][(cycle_count%40)+1:]
    cycle_count += 1

    # Store X if cycle is interesting
    if cycle_count in interesting_dict.keys(): interesting_dict[cycle_count] = X

    # If addx do all again in new cycle, and update X and valid indexes
    if line.split(" ")[0] == "addx":
        if int(cycle_count%40) in valid_list: screen_matrix[int(cycle_count/40)] = screen_matrix[int(cycle_count/40)][0:(cycle_count%40)]+"@"+screen_matrix[int(cycle_count/40)][(cycle_count%40)+1:]
        valid_list = validList(valid_list[0]+int(line.split(" ")[1]))
        cycle_count += 1
        if cycle_count in interesting_dict.keys(): interesting_dict[cycle_count] = X
        X += int(line.split(" ")[1])
print("Part1: %s"%sum(map(lambda a,b: a*b,interesting_dict.keys(),interesting_dict.values())))
print("Part2:")
for line in screen_matrix:
    print(" ".join(line)) #this method puts a space between each character