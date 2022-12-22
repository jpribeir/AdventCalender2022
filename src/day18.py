# Day 18 of the 2022 Advent of Code
# Read input file
with open("../include/example18.inc","r") as coords_file:
#with open("../include/input18.inc","r") as coords_file:
    coords_list = list(map(lambda a: tuple(a.strip().split(",")),coords_file.readlines()))

for i,each in enumerate(coords_list): coords_list[i] = tuple(map(lambda a: int(a),coords_list[i]))
min_coords = [100,100,100]
max_coords = [0,0,0]
total_area = 0
for i,each in enumerate(coords_list):
    for j,_ in enumerate(min_coords):
        min_coords[j] = min(min_coords[j],each[j])
        max_coords[j] = max(max_coords[j],each[j])
    total_area += 6
    # Compare each cube with all next cubes: cubes are side by side only if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) = 1
    for cube in coords_list[i+1:]:
        if sum(map(lambda a,b: abs(a-b), each, cube)) == 1: total_area -= 2

empty_count = 0
for x in range(min_coords[0]+1,max_coords[0]):
    for y in range(min_coords[1]+1,max_coords[1]):
        for z in range(min_coords[2]+1,max_coords[2]):
            print((x,y,z))
            if (x,y,z) not in coords_list: empty_count += 1
print(coords_list)

print("Part1: %s"%total_area)
print("Part2: %s"%empty_count)