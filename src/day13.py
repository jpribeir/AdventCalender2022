# Day 13 of the 2022 Advent of Code
# Read input file
#with open("../include/input13.inc","r") as packet_file:
with open("../include/example13.inc","r") as packet_file:
    packet_list = list(map(lambda a: a.strip(),packet_file.readlines()))

left_list = []
right_list = []
for i in range(0,len(packet_list),3):
    left_list.append(packet_list[i])
    right_list.append(packet_list[i+1])

for i in range(len(left_list)):
    print("###")

#print("Part1: %s"%cost_count)
#print("Part2: %s"%hike_count)