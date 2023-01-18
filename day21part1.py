import re

vals = {}
f = open("day21.txt", "r")
L = f.readlines()
n = 1
print(f"Starting with input with {len(L)} lines")
while len(L) != 0:
    used_indices = []
    for i in range(len(L)):
        line = L[i]
        names = [x for x in re.findall(r"[a-zA-Z]+", line)]
        digits = [int(x) for x in re.findall(r"\d+", line)]
        if len(digits) == 1:
            # register this monkey's value
            vals[names[0]] = digits[0]
            # no longer need this line
            used_indices.append(i)
        else:
            # this monkey performs an operation
            a = names[1]
            b = names[2]
            operand = re.findall(r"[\*\+\/\-]+", line)[0]
            if a in vals and b in vals:
                vals[names[0]] = eval(f"{vals[a]}{operand}{vals[b]}")
                used_indices.append(i)
            # otherwise, skip and wait for both values to appear
    L = [L[i] for i in range(len(L)) if i not in used_indices]
    print(f"Pass {n} done. {len(L)} lines remain")
    n += 1
print(vals["root"])
