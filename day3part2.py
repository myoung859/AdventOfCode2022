from itertools import islice

total_score = 0


with open("day3.txt", "r") as f:
    lines_gen = islice(f, 3)
    while True:
        lines = list(islice(f, 3))
        if lines:
            print(lines[0][:-1])
            item = list(
                set(lines[0][:-1])
                .intersection(lines[1][:-1])
                .intersection(lines[2][:-1])
            )[0]
            if item.isupper():
                total_score += ord(item) - ord("A") + 27
            else:
                total_score += ord(item) - ord("a") + 1
        else:
            break
print(total_score)
f.close()