# Day 10 of the 2022 Advent of Code
def validList(num):
    return list(range(num,num+3))

def part1():
    X = 1
    cycle_count = 0
    for line in cycle_list:
        cycle_count += 1
        if cycle_count in interesting_dict.keys(): interesting_dict[cycle_count] = X
        if line.split(" ")[0] == "addx":
            cycle_count += 1
            if cycle_count in interesting_dict.keys(): interesting_dict[cycle_count] = X
            X += int(line.split(" ")[1])
    return sum(map(lambda a,b: a*b,interesting_dict.keys(),interesting_dict.values()))

def part2():
    screen_matrix = ["."*40]*6
    valid_list = validList(0)
    cycle_count = 0
    for line in cycle_list:
        if int(cycle_count%40) in valid_list: screen_matrix[int(cycle_count/40)] = screen_matrix[int(cycle_count/40)][0:(cycle_count%40)]+"#"+screen_matrix[int(cycle_count/40)][(cycle_count%40)+1:]
        cycle_count += 1
        if line.split(" ")[0] == "addx":
            if int(cycle_count%40) in valid_list: screen_matrix[int(cycle_count/40)] = screen_matrix[int(cycle_count/40)][0:(cycle_count%40)]+"#"+screen_matrix[int(cycle_count/40)][(cycle_count%40)+1:]
            valid_list = validList(valid_list[0]+int(line.split(" ")[1]))
            cycle_count += 1
    for line in screen_matrix: print(line)

# Read input file
with open("../include/input10.inc","r") as cycle_file:
    cycle_list = list(map(lambda a: a.strip(),cycle_file.readlines()))

interesting_dict = {20:0,
                    60:0,
                    100:0,
                    140:0,
                    180:0,
                    220:0}

print("Part1: %s"%part1())
print("\nPart2:")
part2()
