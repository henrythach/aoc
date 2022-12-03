rows = [line.strip().split(' ') for line in open('./input.in', 'r')]

# part 1
# x, y = 0, 0
# for [direction, value] in rows:
#     value = int(value)
#     if direction == 'forward':
#         x += value
#     elif direction == 'down':
#         y += value
#     elif direction == 'up':
#         y -= value
# print(x * y)

# part 2
total = 0
x, y = 0, 0
for [direction, value] in rows:
    value = int(value)
    if direction == 'forward':
        x += value
        total += value * y
    else:
        y += value if direction == 'down' else -value
print(x * total)
