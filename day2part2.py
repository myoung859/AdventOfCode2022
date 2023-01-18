outcome_scores = {"X": 0, "Y": 3, "Z": 6}
move_scores = {"A": 1, "B": 2, "C": 3}
losses = {"A": "C", "B": "A", "C": "B"}
wins = {"C": "A", "A": "B", "B": "C"}

total_score = 0
f = open("day2.txt", "r")
for line in f.readlines():
    opp_move = line[0]
    outcome = line[2]
    if outcome == "X":
        my_move = losses[opp_move]
    elif outcome == "Z":
        my_move = wins[opp_move]
    else:
        my_move = opp_move
    total_score += outcome_scores[outcome] + move_scores[my_move]

f.close()
print(total_score)