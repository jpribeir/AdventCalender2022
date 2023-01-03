# Day 12 of the 2022 Advent of Code
# Return x,y point where character is found
def findChar(char):
    for i,line in enumerate(heightmap_matrix):
        if char in line:
            for j,letter in enumerate(line):
                if letter==char: return i,j

# Return unicode code for character
def heightVal(char):
    if char=="S": return ord("a")
    elif char=="E": return ord("z")
    else: return ord(char)

# Read input file
with open("../include/input12.inc","r") as heightmap_file:
    heightmap_matrix = list(map(lambda a: a.strip(),heightmap_file.readlines()))
maxX = len(heightmap_matrix)
maxY = len(heightmap_matrix[0])

# Search START position
startX,startY = findChar("S")
to_visit_list = [(startX,startY)]
visited_list = []
path_found = False
cost_count = 0
while not path_found:
    next_list = []
    # Visit all valid points in this loop
    for x,y in to_visit_list:
        # Count loops until END is found
        if heightmap_matrix[x][y] == "E":
            cost_count -= 1
            path_found = True
            break
        
        # Add valid neighbours to list to be visited next loop
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (x+i) in range(maxX) and (y+j) in range(maxY) and (x+i,y+j) not in visited_list:
                if heightVal(heightmap_matrix[x+i][y+j])-heightVal(heightmap_matrix[x][y])<=1:
                    if (x+i,y+j) not in next_list: next_list.append((x+i,y+j))
        visited_list.append((x,y))
    cost_count += 1
    to_visit_list = next_list.copy()

# Search END position
endX,endY = findChar("E")
to_visit_list = [(endX,endY)]
visited_list = []
path_found = False
hike_count = 0
while not path_found:
    next_list = []
    # Visit all valid points in this loop
    for x,y in to_visit_list:
        # Count loops until lower point is found
        if heightVal(heightmap_matrix[x][y]) == ord("a"):
            hike_count -= 1
            path_found = True
            break

        # Add valid neighbours to list to be visited next loop
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (x+i) in range(0,maxX) and (y+j) in range(0,maxY) and (x+i,y+j) not in visited_list:
                if heightVal(heightmap_matrix[x+i][y+j])-heightVal(heightmap_matrix[x][y])>=-1:
                    if (x+i,y+j) not in next_list: next_list.append((x+i,y+j))
        visited_list.append((x,y))
    hike_count += 1
    to_visit_list = next_list.copy()

print("Part1: %s"%cost_count)
print("Part2: %s"%hike_count)