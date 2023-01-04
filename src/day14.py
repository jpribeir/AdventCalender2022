# Day 14 of the 2022 Advent of Code
# Read input file
with open("../include/input14.inc","r") as rock_file:
#with open("../include/example14.inc","r") as rock_file:
    rock_list = list(map(lambda a: a.strip(),rock_file.readlines()))

max_coords = [0,0]
min_coords = [1000,1000]
wall_list = []
for line in rock_list:
    wall_list.append(line.split(" -> "))
    for point in wall_list[-1]:
        for j in range(2):
            max_coords[j] = max(max_coords[j],int(point.split(",")[j]))
            min_coords[j] = min(min_coords[j],int(point.split(",")[j]))
print(wall_list)
print(max_coords)
print(min_coords)

cave_matrix = [ "."*(max_coords[0]-min_coords[0]) ]*max_coords[1]

for line in cave_matrix: print(line)

#print("Part1: %s"%cost_count)
#print("Part2: %s"%hike_count)