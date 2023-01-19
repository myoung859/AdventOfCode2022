import re  # here we go with regex.

total_pairs = 0  # ones where one fully contains the other

overlaps = 0  # i.e. they intersect at all

f = open("day4.txt", "r")
for line in f.readlines():
    digits = [int(x) for x in re.findall(r"\d+", line)]
    # should always be 4 numbers...at least, for part 1
    first_range = set(range(digits[0], digits[1] + 1))
    second_range = set(range(digits[2], digits[3] + 1))

    intersect = first_range.intersection(second_range)
    if intersect == first_range or intersect == second_range:
        # print(intersect, first_range, second_range)
        total_pairs += 1
        overlaps += 1
    elif len(intersect) != 0:
        # print(intersect)
        overlaps += 1
print(f"Number of pairs with complete overlap: {total_pairs}")
print(f"Number of pairs with any overlap: {overlaps}")
f.close()