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
        return moveInDirection(i+incr_i,j+incr_j,incr_i,incr_j,min_height)
    else:
        view_count += 1
        return False,view_count

# Check line of sight in all 4 basic directions
def checkVisability(i,j):
    for incr_i,incr_j in [(-1,0),(0,1),(1,0),(0,-1)]:
        view_count = 1
        if tree_matrix[i][j]>tree_matrix[i+incr_i][j+incr_j]:
            if moveInDirection(i+incr_i,j+incr_j,incr_i,incr_j,tree_matrix[i][j],view_count): return True
    else: return False

# Read input file
with open("../include/example8.inc","r") as tree_file:
#with open("../include/input8.inc","r") as tree_file:
    tree_matrix = list(map(lambda a: a.strip(),tree_file.readlines()))

max_i = len(tree_matrix)-1
max_j = len(tree_matrix[0])-1
#hidden_matrix = [ [ False ] * max_j ] * max_i
visible_count = 0
for i,line in enumerate(tree_matrix):
    for j,tree in enumerate(line):
        #print("### %s,%s ###"%(i,j))
        if foundEdge(i,j): visible_count += 1
        elif checkVisability(i,j): visible_count += 1
        #else: hidden_matrix[i][j] = True

print("Part1: %s"%visible_count)
#print("Part2: %s"%visible_count)