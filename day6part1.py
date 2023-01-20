f = open("day6.txt", "r")
L = f.readline()
# L = "bvwbjplbgvbhsrlpgdmjqwftvncz"
i = 0
while i < len(L) - 14:
    s = set(L[i : i + 14])
    if len(s) == 14:
        print(i + 14)
        print(L[i : i + 14])
        print(s)
        break
    i += 1
f.close()