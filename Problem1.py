max = 0
total = 0
f = open("day1.txt", "r")
for line in f.readlines():
    if line != "\n":
        total += int(line)
    else:
        if total > max:
            max = total
        total = 0
f.close()
print(max)