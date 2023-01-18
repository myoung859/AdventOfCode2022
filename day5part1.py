import re

"""
for i in range(n):
    crates[dest].extend(crates[source].pop())
"""

crates = []
f = open("day5.txt", "r")
for line in f.readlines():
    if "move" in line:
        digits = [int(x) for x in re.findall(r"\d+", line)]
        n = digits[0]
        source = digits[1]
        dest = digits[2]
        for i in range(n):
            crates[dest].extend(crates[source].pop())

message = [c[-1] for c in crates]
print("".join(message))