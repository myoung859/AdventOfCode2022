import re
from copy import copy

vals = {}
f = open("day21.txt", "r")
L = f.readlines()
n = 1
print(f"Starting with input with {len(L)} lines")


def test_eval(L_test, val_dict, humn_guess):
    # part 2 is essentially finding the 0 of this function
    val_dict["humn"] = humn_guess
    while len(L_test) != 0:
        used_indices = []
        for i in range(len(L_test)):
            line = L_test[i]
            names = [x for x in re.findall(r"[a-zA-Z]+", line)]
            digits = [int(x) for x in re.findall(r"\d+", line)]
            if len(digits) == 1:
                # register this monkey's value
                val_dict[names[0]] = digits[0]
                # no longer need this line
                used_indices.append(i)
            else:
                # this monkey performs an operation
                a = names[1]
                b = names[2]
                operand = re.findall(r"[\*\+\/\-]+", line)[0]
                if a in val_dict and b in val_dict:
                    if names[0] == "root":
                        return (
                            val_dict[a] - val_dict[b]
                        )  # if this is 0, we've found the right humn value
                    val_dict[names[0]] = eval(f"{val_dict[a]}{operand}{val_dict[b]}")
                    used_indices.append(i)
                # otherwise, skip and wait for both values to appear
        if len(used_indices) == 0:
            break
        else:
            L_test = [L_test[i] for i in range(len(L_test)) if i not in used_indices]


# simplify inputs that don't rely on humn
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
            if a in vals and b in vals and "humn" not in [a, b]:
                vals[names[0]] = eval(f"{vals[a]}{operand}{vals[b]}")
                used_indices.append(i)
            # otherwise, skip and wait for both values to appear
    if len(used_indices) == 0:
        print(f"Pass {n} done. {len(L)} lines remain")
        break
    else:
        L = [L[i] for i in range(len(L)) if i not in used_indices]
        print(f"Pass {n} done. {len(L)} lines remain")
        n += 1
test_vals = copy(vals)
# print(test_eval(copy(L), test_vals, 1e15))

left = 0  # known to yield result greater than 0
right = 1e15  # tested to be less than 0

while abs(left - right) >= 1.01:
    print(abs(left - right))
    m = (left + right) // 2
    f = test_eval(copy(L), copy(test_vals), m)
    if abs(f) <= 1e-9:
        break
    elif f < 0:
        right = m
    else:
        left = m
print(f"value found via binary search: {m}")

# alternatively...use the secant method to do it in nearly one shot
# not sure why this takes 2 iterations instead of one, given that the function is linear
x0 = 0
x1 = 1e15
MAX_ITER = 50
n = 1
print("Secant Method")
while n <= MAX_ITER:
    print(f"Iteration {n}")
    x2 = x1 - test_eval(copy(L), copy(test_vals), x1) * (x1 - x0) / (
        test_eval(copy(L), copy(test_vals), x1)
        - test_eval(copy(L), copy(test_vals), x0)
    )
    f = test_eval(copy(L), copy(test_vals), x2)
    if abs(f) <= 1e-9:
        break
    else:
        x0, x1 = x1, x2
    n += 1


print(f"value found via secant method: {x2}")