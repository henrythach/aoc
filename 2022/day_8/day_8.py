trees = [[int(col) for col in row] for row in open('./sample.txt', 'r').read().split()]
visible = [[0 for col in range(len(trees))] for row in range(len(trees))]

print(trees)
print(visible)

# edges are always visible
for i in range(len(trees)):
    visible[i][0] = 1
    visible[i][-1] = 1
    visible[0][i] = 1
    visible[-1][i] = 1

print('before')
print(visible)

# left-to-right
for i in range(1, len(trees) - 1):
    left_max = trees[i][0]
    for j in range(1, len(trees) - 1):
        curr = trees[i][j]
        if curr > left_max:
            visible[i][j] |= 1
        left_max = max(left_max, curr)

# right-to-left
for i in range(1, len(trees) - 1):
    right_max = trees[~i][-1]
    for j in range(1, len(trees) - 1):
        curr = trees[~i][~j]
        if curr > right_max:
            visible[~i][~j] |= 1
        right_max = max(right_max, curr)

# top-to-bottom
for i in range(1, len(trees) - 1):
    top_max = trees[0][i]
    for j in range(1, len(trees) - 1):
        curr = trees[j][i]
        if curr > top_max:
            visible[j][i] |= 1
        top_max = max(top_max, curr)

# bottom-to-top
for i in range(1, len(trees) - 1):
    bottom_max = trees[-1][i]
    for j in range(1, len(trees) - 1):
        curr = trees[~j][i]
        if curr > bottom_max:
            visible[~j][i] |= 1
        bottom_max = max(bottom_max, curr)

print('after')
for row in visible:
    print(row)

print(sum(col for row in visible for col in row))
