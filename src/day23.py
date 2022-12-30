# Day 23 of the 2022 Advent of Code
# Extend matrix x rows and columns 
def expandMatrix(original_matrix,num_extra):
    num_original = len(original_matrix[0])
    elfs_matrix = [ "."*(num_original+2*num_extra)]*num_extra
    for line in original_matrix: elfs_matrix.append("."*num_extra+line+"."*num_extra)
    for i in range(num_extra): elfs_matrix.append("."*(num_original+2*num_extra))
    return elfs_matrix

def prepareMoves():
    point_matrix = [ [0]*len(elfs_matrix) ]*len(elfs_matrix)
    for i,row in enumerate(point_matrix):
        for j,col in enumerate(row):
            if elfs_matrix[i][j]=="#": point_matrix[i][j] = 1
    for i,row in enumerate(elfs_matrix):
        for j,col in enumerate(row):
            if col=="#":
                do_move = False
                for ii,jj in neighbours_list:
                    if elfs_matrix[i+ii][j+jj] = "#":
                        do_move = True
                        break
            if do_move:
                for addX,addY in cardinals_list:
                    if "#" not in point_matrix[i+addX][j+addY]


# Read input file
with open("../include/example23.inc","r") as elfs_file:
#with open("../include/input23.inc","r") as elfs_file:
    original_matrix = list(map(lambda a: a.strip(),elfs_file.readlines()))

num_turns = 10
elfs_matrix = expandMatrix(original_matrix,num_turns)
for each in elfs_matrix: print(each)

prepareMoves()

neighbours_list = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
cardinals_list = [(-1,0),(1,0),(0,-1),(0,1)]
for turn in range(num_turns):
    print("")
    cardinals_list = cardinals_list[1:] + cardinals_list[:1]

#print("Part1: %s"%total_area)
#print("Part2: %s"%empty_count)