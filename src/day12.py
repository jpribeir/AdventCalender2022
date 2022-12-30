# Day 12 of the 2022 Advent of Code
def findChar(char):
    for i,line in enumerate(heightmap_matrix):
        if char in line:
            for j,letter in enumerate(line):
                if letter==char: return i,j

def heightVal(char):
    if char=="S": return ord("a")
    elif char=="E": return ord("z")
    else: return ord(char)

def changeMap(visited_matrix,x,y,char):
    newly_visited_matrix = visited_matrix.copy()
    newly_visited_matrix[x] = newly_visited_matrix[x][0:y]+char+newly_visited_matrix[x][y+1:]
    return newly_visited_matrix

def nextSpot(x,y,lenval,visited_matrix,prevX,prevY,lowest_path):
    if lenval + sum(map(lambda a,b: abs(a-b), [endX,endY],[x,y])) < lowest_path:
        #print("## %s,%s ##"%(x,y))
        newly_visited_matrix = changeMap(visited_matrix,x,y,"#")
        #if x==prevX and y==prevY: newly_visited_matrix = changeMap(visited_matrix,x,y,"E")
        #elif x-prevX==1: newly_visited_matrix = changeMap(visited_matrix,x,y,"^")
        #elif x-prevX==-1: newly_visited_matrix = changeMap(visited_matrix,x,y,"v")
        #elif y-prevY==1: newly_visited_matrix = changeMap(visited_matrix,x,y,"<")
        #elif y-prevY==-1: newly_visited_matrix = changeMap(visited_matrix,x,y,">")
        #print(newly_visited_matrix)
        if heightmap_matrix[x][y]=="S":
            #print("## %s ##"%lenval)
            #for each in newly_visited_matrix: print(each)
            return lenval
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            #print(">%s,%s"%(x+i,x+j))
            if (x+i) in range(0,maxX) and (y+j) in range(0,maxY) and newly_visited_matrix[x+i][y+j]==".":
                if heightVal(heightmap_matrix[x+i][y+j])-heightVal(heightmap_matrix[x][y])>=-1:
                    lowest_path = min(lowest_path,nextSpot(x+i,y+j,lenval+1,newly_visited_matrix,x,y,lowest_path))
    return lowest_path

# Read input file
#with open("../include/example12.inc","r") as heightmap_file:
with open("../include/input12.inc","r") as heightmap_file:
    heightmap_matrix = list(map(lambda a: a.strip(),heightmap_file.readlines()))

maxX = len(heightmap_matrix)
maxY = len(heightmap_matrix[0])
visited_matrix = ["."*maxY]*maxX
startX,startY = findChar("E")
endX,endY = findChar("S")
print("Part1: %s"%nextSpot(startX,startY,0,visited_matrix,startX,startY,maxX*maxY))