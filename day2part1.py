move_scores = {"A": 1, "B": 2, "C": 3}
wins = {"A": "C", "B": "A", "C": "B"}
total_score = 0
f = open("day2.txt", "r")
for line in f.readlines():
    opp_move = line[0]

    my_move = chr(ord(line[2]) - 23)  # to move back to A,B,C
    if opp_move == wins[my_move]:
        round_score = 6
    elif opp_move == my_move:
        round_score = 3
    else:
        round_score = 0
    total_score += round_score + move_scores[my_move]


f.close()
print(total_score)