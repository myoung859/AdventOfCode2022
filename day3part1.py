total_score = 0

f = open("day3.txt", "r")
for line in f.readlines():
    first, second = line[: len(line) // 2], line[len(line) // 2 : -1]
    item = list(set(first).intersection(second))[0]
    if item.isupper():
        total_score += ord(item) - ord("A") + 27
    else:
        total_score += ord(item) - ord("a") + 1
print(total_score)
f.close()