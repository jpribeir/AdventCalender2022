# Day 14 of the 2022 Advent of Code
# Build cave based on wall list
def buildCave(wall_list):
    cave_matrix = [ "."*(max_coords[0]-min_coords[0]+1) ]*(max_coords[1]+1)
    for wall in wall_list:
        wallstart = tuple(map(lambda x,y: int(x)-y,wall[0].split(","),[min_coords[0],0]))
        for i in range(1,len(wall)):
            wallend = tuple(map(lambda x,y: int(x)-y,wall[i].split(","),[min_coords[0],0]))
            if wallstart[0]==wallend[0]:
                if wallstart[1]<wallend[1]: x,y = wallstart[0],range(wallstart[1],wallend[1]+1)
                else: x,y = wallstart[0],range(wallend[1],wallstart[1]+1)
            else:
                if wallstart[0]<wallend[0]: x,y = range(wallstart[0],wallend[0]+1),wallstart[1]
                else: x,y = range(wallend[0],wallstart[0]+1),wallstart[1]
            try:
                for j in x: cave_matrix[y] = cave_matrix[y][0:j]+"#"+cave_matrix[y][j+1:]
            except:
                for j in y: cave_matrix[j] = cave_matrix[j][0:x]+"#"+cave_matrix[j][x+1:]
            wallstart = wallend
    return cave_matrix

# Start dropping sand and count until sand falls off to abyss
def fillCave():
    sand_count = 0
    drop_point = [500-min_coords[0]+1,0]
    while True:
        sand_moving = True
        x,y = drop_point[0],drop_point[1]
        while sand_moving:
            if cave_matrix[y+1][x] == ".": y += 1
            elif cave_matrix[y+1][x] == "!": return sand_count
            elif cave_matrix[y+1][x-1] == ".": y,x = y+1,x-1
            elif cave_matrix[y+1][x-1] == "!": return sand_count
            elif cave_matrix[y+1][x+1] == ".": y,x = y+1,x+1
            elif cave_matrix[y+1][x+1] == "!": return sand_count
            else:
                sand_moving = False
                cave_matrix[y] = cave_matrix[y][0:x]+"o"+cave_matrix[y][x+1:]
                sand_count += 1
                if x==drop_point[0] and y==drop_point[1]: return sand_count
    

# Read input file
with open("../include/input14.inc","r") as rock_file:
    rock_list = list(map(lambda a: a.strip(),rock_file.readlines()))

# Parse points to form rock walls and define max and min coordinates
max_coords = [0,0]
min_coords = [1000,1000]
wall_list = []
for line in rock_list:
    wall_list.append(line.split(" -> "))
    for point in wall_list[-1]:
        for j in range(len(max_coords)):
            max_coords[j] = max(max_coords[j],int(point.split(",")[j]))
            min_coords[j] = min(min_coords[j],int(point.split(",")[j]))

# Part1: after building walls, add "!" to detect out of bounds spots
cave_matrix = buildCave(wall_list)
for i,line in enumerate(cave_matrix): cave_matrix[i] = "!"+line+"!"
cave_matrix.append("!"*len(cave_matrix[0]))
print("Part1: %s"%fillCave())
for line in cave_matrix: print(line)

# Part2: after building walls, extend each side at least the same distance as the cave height
cave_matrix = buildCave(wall_list)
for i,line in enumerate(cave_matrix): cave_matrix[i] = ("."*max_coords[1])+line+("."*max_coords[1])
cave_matrix.append("."*len(cave_matrix[0]))
cave_matrix.append("#"*len(cave_matrix[0]))
max_coords[0] += max_coords[1]
min_coords[0] -= max_coords[1]
max_coords[1] += 2
print("Part2: %s"%fillCave())
for line in cave_matrix: print(line)