# Day 15 of the 2022 Advent of Code
import re

# Calculate Manhattan distance
def calcDist(x,y,w,z):
    return abs(x-w)+abs(y-z)

# Add up set of spots closer to sensor than closest beacon
def checkCoord(initial_col,spot_count):
    for x,y in sensor_dict:
        if calcDist(x,y,initial_col,row_check) <= sensor_dict[(x,y)]:
            extra = x-initial_col + sensor_dict[(x,y)] - abs(y-row_check)+1
            new_col = initial_col+extra
            extra -= len(list(set(range(initial_col,new_col)) & set(row_beacon_list)))
            return new_col,spot_count+extra
    else: return initial_col+1,spot_count

# Read input file
with open("../include/input15.inc","r") as coords_file:
    coords_list = list(map(lambda a: a.strip(),coords_file.readlines()))

row_check = 2000000
min_coords,max_coords = [0,0],[0,0]
sensor_dict = {}
row_beacon_list = []
for line in coords_list:
    coords = re.search(r"^Sensor at x\=(.*), y\=(.*): closest beacon is at x\=(.*), y\=(.*)$",line)
    max_dist = calcDist(int(coords.group(1)),int(coords.group(2)),int(coords.group(3)),int(coords.group(4)))
    sensor_dict[(int(coords.group(1)),int(coords.group(2)))] = max_dist
    if int(coords.group(4))==row_check: row_beacon_list.append(int(coords.group(3)))
    for i,_ in enumerate(max_coords):
        min_coords[i] = min(min_coords[i],int(coords.group(i+1))-max_dist)
        max_coords[i] = max(max_coords[i],int(coords.group(i+1))+max_dist)

spot_count = 0
col = min_coords[0]
while col <= max_coords[0]:
    col,spot_count = checkCoord(col,spot_count)

print("Part1: %s"%spot_count)