# Day 18 of the 2022 Advent of Code
# Read input file
with open("../include/input18.inc","r") as coords_file:
    coords_list = list(map(lambda a: tuple(a.strip().split(",")),coords_file.readlines()))

total_area = 0
for i,each in enumerate(coords_list):
    total_area += 6
    # Compare each cube with all next cubes: cubes are side by side only if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) = 1
    for cube in coords_list[i+1:]: if sum(map(lambda a,b: abs(int(a)-int(b)), each, cube)) == 1: total_area -= 2

print("Part1: %s"%total_area)