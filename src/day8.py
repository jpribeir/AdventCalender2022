# Day 8 of the 2022 Advent of Code
# Check if coordenates are on the edge
def foundEdge(i,j):
    if i == 0 or i == max_i or j == 0 or j == max_j: return True
    else: return False

# Continue comparing to the next element in the same direction
def moveInDirection(i,j,incr_i,incr_j,min_height,view_count):
    if foundEdge(i,j): return True,view_count
    elif tree_matrix[i+incr_i][j+incr_j]<min_height:
        view_count += 1
        return moveInDirection(i+incr_i,j+incr_j,incr_i,incr_j,min_height,view_count)
    else: return False,view_count+1

# Check line of sight in all 4 basic directions
def checkVisability(i,j):
    is_visible = False
    view_factor = 1
    for incr_i,incr_j in [(-1,0),(0,1),(1,0),(0,-1)]:
        if tree_matrix[i][j]>tree_matrix[i+incr_i][j+incr_j]:
            found_view,view_count = moveInDirection(i+incr_i,j+incr_j,incr_i,incr_j,tree_matrix[i][j],1)
            if found_view: is_visible = True
            view_factor *= view_count
    return is_visible,view_factor

# Read input file
with open("../include/input8.inc","r") as tree_file:
    tree_matrix = list(map(lambda a: a.strip(),tree_file.readlines()))

max_i , max_j = len(tree_matrix)-1 , len(tree_matrix[0])-1
visible_count , max_view = 0 , 1 

# Go through each tree in each line
for i,line in enumerate(tree_matrix):
    for j,tree in enumerate(line):
        if foundEdge(i,j): visible_count += 1
        else:
            is_visible,view_factor = checkVisability(i,j)
            if is_visible: visible_count += 1
            max_view = max(max_view,view_factor)

print("Part1: %s"%visible_count)
print("Part2: %s"%max_view)