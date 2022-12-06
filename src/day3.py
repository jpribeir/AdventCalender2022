# Day 3 of the 2022 Advent of Code
# Find common item in group of sacks
def groupIntersect(current,rest_group):
    common_set = set(current).intersection(rest_group[0])
    # If there are still sacks to compare, re-enter the function
    if len(rest_group)>1: return groupIntersect(common_set,rest_group[1:])
    return list(common_set)[0]

# Convert item type to correct code number
def convertCode(item_type):
    # Unicode table
    Aup = 65
    Zup = 90
    Alow = 97
    Zlow = 122
    priority = ord(item_type)
    if priority in range(Aup,Zup+1): return priority-38
    elif priority in range(Alow,Zlow+1): return priority-96

# Read input file
with open("../include/input3.inc","r") as sack_file:
    sack_list = list(map(lambda a: a.strip(),sack_file.readlines()))

# Compare each sack's halves
total_priority = 0
for sack in sack_list:
    partA = sack[0:int(len(sack)/2)]
    partB = sack[int(len(sack)/2):]
    total_priority += convertCode(groupIntersect(partA,[partB]))

# Group sacks into groups of <num_elfs>
group_list = []
num_elfs = 3
for sack in range(0,len(sack_list)-num_elfs+1,num_elfs): group_list.append(sack_list[sack:sack+num_elfs])

# Go through each group of sacks
group_priority = 0
for group in group_list: group_priority += convertCode(groupIntersect(group[0],group[1:]))

print("Part1: %s"%total_priority)
print("Part2: %s"%group_priority)