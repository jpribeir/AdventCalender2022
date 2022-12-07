# Day 4 of the 2022 Advent of Code
# Return list of regions
def getRegions(rangeIDs):
    startID = int(rangeIDs.split("-")[0])
    endID = int(rangeIDs.split("-")[1])
    return range(startID,endID+1)

# Check if list of regions is all contained in another
def areContained(elfA,elfB):
    if all(item in getRegions(elfA) for item in getRegions(elfB)) or all(item in getRegions(elfB) for item in getRegions(elfA)): return 1
    else: return 0

# Check if any region is in both list
def overlapAtAll(elfA,elfB):
    if any(item in getRegions(elfA) for item in getRegions(elfB)): return 1
    else: return 0

# Read input file
with open("../include/input4.inc","r") as pair_file:
    pair_list = list(map(lambda a: a.strip(),pair_file.readlines()))

contain_count = 0
overlap_count = 0
for pair in pair_list:
    elfA = pair.split(",")[0]
    elfB = pair.split(",")[1]
    contain_count += areContained(elfA,elfB)
    overlap_count += overlapAtAll(elfA,elfB)

print("Part1: %s"%contain_count)
print("Part2: %s"%overlap_count)