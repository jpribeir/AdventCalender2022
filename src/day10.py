# Day 10 of the 2022 Advent of Code
def validList(num):
    return range(num,num+3)

# Read input file
#with open("../include/input10.inc","r") as cycle_file:
with open("../include/example10.inc","r") as cycle_file:
    cycle_list = list(map(lambda a: a.strip(),cycle_file.readlines()))

interesting_dict = {20:0,
                    60:0,
                    100:0,
                    140:0,
                    180:0,
                    220:0}
X = 1
cycle_count = 0
for line in cycle_list:
    cycle_count += 1
    if cycle_count in interesting_dict.keys(): interesting_dict[cycle_count] = X
    if line.split(" ")[0] == "addx":
        cycle_count += 1
        if cycle_count in interesting_dict.keys(): interesting_dict[cycle_count] = X
        X += int(line.split(" ")[1])
print("Part1: %s"%sum(map(lambda a,b: a*b,interesting_dict.keys(),interesting_dict.values())))

screen_matrix = ["."*40]*6
print(screen_matrix)
valid_list = validList(0)
cycle_count = 0
for line in cycle_list:
    print("### %s"%line)
    print(int(cycle_count/40))
    if cycle_count in valid_list:
        #aux = screen_matrix[int(cycle_count/40)].copy()
        #aux[cycle_count%40] = "#"
        #screen_matrix[int(cycle_count/40)] = aux.copy()
        #screen_matrix[int(cycle_count/40)][cycle_count%40] = "#"
        screen_matrix[int(cycle_count/40)] = screen_matrix[int(cycle_count/40)][0:cycle_count%40]+"#"+screen_matrix[int(cycle_count/40)+1][cycle_count%40:]
    cycle_count += 1
    if line.split(" ")[0] == "addx":
        if cycle_count in valid_list:
            #aux = screen_matrix[int(cycle_count/40)].copy()
            #aux[cycle_count%40] = "#"
            #screen_matrix[int(cycle_count/40)] = aux.copy()
            #screen_matrix[int(cycle_count/40)][cycle_count%40] = "#"
            screen_matrix[int(cycle_count/40)] = screen_matrix[int(cycle_count/40)][0:cycle_count%40]+"#"+screen_matrix[int(cycle_count/40)][cycle_count%40:]
        valid_list = validList(valid_list[0]+int(line.split(" ")[1]))
        cycle_count += 1

print("\nPart2:")
for line in screen_matrix: print(line)