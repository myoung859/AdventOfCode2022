sums = []
max = 0
total = 0
f = open("day1.txt", "r")
for line in f.readlines():
    if line != "\n":
        total += int(line)
    else:
        if total > max:
            max = total
        sums.append(total)
        total = 0
# to remember the last one
sums.append(total)
f.close()
sums.sort()
# print(max in sums)
print(sum(sums[-3:]))