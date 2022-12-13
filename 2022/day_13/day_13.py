from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        else:
            return -1 if left < right else 1

    i = 0
    while i < len(left) and i < len(right):
        c = compare(left[i], right[i])
        if c < 0 or c > 0:
            return c
        i += 1

    if i == len(left) and i < len(right):
        return -1
    elif i < len(left) and i == len(right):
        return 1

    return 0


# print(compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))  # True
# print(compare([7, 7, 7, 7], [7, 7, 7]))  # False
# print(compare([[1], [2, 3, 4]], [[1], 4]))  # True


data = open('input.txt', 'r').read().strip()

# part 1
p1 = 0
pairs = [[eval(signal) for signal in pair.split('\n')] for pair in data.split('\n\n')]
for index, pair in enumerate(pairs):
    a, b = pair
    if compare(a, b) == -1:
        p1 += index + 1
print(p1)


# part 2
pp = [[[2]], [[6]]]
for pair in pairs:
    pp.append(pair[0])
    pp.append(pair[1])
p2 = []
for i, p in enumerate(sorted(pp, key=cmp_to_key(compare))):
    if p == [[2]] or p == [[6]]:
        p2.append(i + 1)
print(p2[0] * p2[1])
