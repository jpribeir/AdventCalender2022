# Day 17 of the 2022 Advent of Code
def shiftPiece(room_list,height,dir):
    if dir=="<":
        for i in range(height):
            if room_list[i][0] == "#" or "&#" in room_list[i]: return room_list
        for i in range(height):
            aux_line = ""
            for j in range(len(room_list[i])-1):
                if room_list[i][j] == "&": aux_line +="&"
                elif room_list[i][j+1] != "&": aux_line += room_list[i][j+1]
                else: aux_line += "."
            if room_list[i][-1] == "&": aux_line +="&"
            else: aux_line += "."
            room_list[i] = aux_line
    else:
        for i in range(height):
            if room_list[i][-1] == "#" or "#&" in room_list[i]: return room_list
        for i in range(height):
            if room_list[i][0] == "&": aux_line = "&"
            else: aux_line = "."
            for j in range(1,len(room_list[i])):
                if room_list[i][j] == "&": aux_line +="&"
                elif room_list[i][j-1] != "&": aux_line += room_list[i][j-1]
                else: aux_line += "."
            room_list[i] = aux_line
    return room_list

def downPiece(room_list,height):
    aux_line = ""
    for j in range(len(room_list[0])):
        if room_list[0][j] == "&": aux_line += "&"
        else: aux_line += "."
    prev_line = room_list[0]
    room_list[0] = aux_line
    in_piece = False
    for i in range(1,height+1):
        aux_line = ""
        for j in range(len(room_list[i])):
            if prev_line[j] == "#": aux_line += "#"
            elif room_list[i][j] == "#":
                in_piece = True
                aux_line += "."
            else: aux_line += room_list[i][j]
        prev_line = room_list[i]
        room_list[i] = aux_line
        if in_piece and ("#" in room_list[i-1]) and ("#" not in room_list[i]): break
    return room_list

# Read input file
with open("../include/input17.inc","r") as pattern_file:
        pattern = pattern_file.read().strip()

piece_list = [["..####."],
              ["...#...","..###..","...#..."],
              ["....#..","....#..","..###.."],
              ["..#....","..#....","..#....","..#...."],
              ["..##...","..##..."]]
chamber_list = ["&"*7]
piece_count = 0
current_piece = 0
while piece_count<2023:
    piece_count += 1
    for _ in range(3): chamber_list.insert(0,"."*7)
    piece_height = len(piece_list[current_piece])
    chamber_list = piece_list[current_piece]+chamber_list
    steps_down_count = 0
    going_down = True
    while going_down:
        chamber_list = shiftPiece(chamber_list.copy(),piece_height+steps_down_count,pattern[0])
        pattern = pattern[1:]+pattern[0]
        for i in range(len(chamber_list)):
            for j in range(7):
                if chamber_list[i][j]=="#" and chamber_list[i+1][j]=="&": going_down = False
        if going_down:
            chamber_list = downPiece(chamber_list.copy(),piece_height+steps_down_count)
            steps_down_count += 1
        else:
            for i in range(piece_height+steps_down_count):
                aux_line = chamber_list[i].replace("#","&")
                chamber_list[i] = aux_line
            for i in range(len(chamber_list)):
                if chamber_list[0] == "."*7: chamber_list.pop(0)
                else: break
            if current_piece >= len(piece_list)-1: current_piece = 0
            else: current_piece += 1
print("Part1: %s"%(len(chamber_list)-1))