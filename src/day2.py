# Day 2 of the 2022 Advent of Code
# Read input file
with open("../include/input2.inc","r") as duel_file:
    duel_list = list(map(lambda a: a.strip(),duel_file.readlines()))

shape_dict = {"A":1,
              "B":2,
              "C":3,
              "X":1,
              "Y":2,
              "Z":3}

score_total1=0
for duel in duel_list:
    c1 = duel[0]
    c2 = duel[2]
    score_total1+=shape_dict[c2]
    if shape_dict[c1] > shape_dict[c2]:
        if shape_dict[c1]==3 and shape_dict[c2]==1: score_total1+=6
    elif shape_dict[c1] == shape_dict[c2]: score_total1+=3
    else:
        if not(shape_dict[c1]==1 and shape_dict[c2]==3): score_total1+=6

match_dict = {"A X":"C",
              "A Z":"B",
              "B X":"A",
              "B Z":"C",
              "C X":"B",
              "C Z":"A"}
result_dict = {"X":0,
               "Y":3,
               "Z":6}
score_total2=0
for duel in duel_list:
    d1 = duel[0]
    d2 = duel[2]
    score_total2+=result_dict[d2]
    if d2=="Y": score_total2+=shape_dict[d1]
    else: score_total2+=shape_dict[match_dict[duel]]

print("Part1: %s"%score_total1)
print("Part2: %s"%score_total2)