# Day 15 of the 2022 Advent of Code
import re

# Read input file
with open("../include/example15.inc","r") as coords_file:
#with open("../include/input15.inc","r") as coords_file:
    coords_list = list(map(lambda a: a.strip(),coords_file.readlines()))

sensor_dict = {}
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
for line in coords_list:
    coords = re.findall("\d+", line)
    sensor_dict[(coords[0],coords[1])] = (coords[2],coords[3])

row_check = 20


#print("Part1: %s"%visible_count)
#print("Part2: %s"%max_view)