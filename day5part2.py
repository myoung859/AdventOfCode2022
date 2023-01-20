import re

crates = [[] for i in range(100)]  # will prune later
f = open("day5.txt", "r")
for line in f.readlines():
    if line[0] == "[" or line[0] == " " and line[1] != "1":  # some hacky parsing
        counter = 0
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                crates[counter].append(line[i])
            counter += 1
    else:
        break
crates = [c[::-1] for c in crates if c != []]
print(sum([len(c) for c in crates]))

f = open("day5.txt", "r")
for line in f.readlines():
    # TODO: parse the initial crate setup
    if "move" in line:
        digits = [int(x) for x in re.findall(r"\d+", line)]
        n = digits[0]
        source = digits[1]
        dest = digits[2]
        crates[dest - 1].extend(crates[source - 1][-n:])
        crates[source - 1] = crates[source - 1][:-n]

print(crates)
print(sum([len(c) for c in crates]))
message = [c[-1] for c in crates if len(c) != 0]
print("".join(message))
f.close()