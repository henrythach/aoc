# Huge thanks goes to William Y. Feng for his explanation
# See: https://www.youtube.com/watch?v=QfSPVrWKGcU

rows = [line.strip().split() for line in open('./input.txt', 'r')]

D = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}


def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


# part 1
# hx, hy, tx, ty = 0, 0, 0, 0
# visited = set()
# visited.add((hx, hy))
# for head_direction, steps in rows:
#     for _ in range(int(steps)):
#         a, b = D[head_direction]
#         hx, hy = hx + a, hy + b
#
#         if not touching(hx, hy, tx, ty):
#             c = 0 if hx == tx else (hx - tx) // abs(hx - tx)
#             d = 0 if hy == ty else (hy - ty) // abs(hy - ty)
#
#             tx, ty = tx + c, ty + d
#             visited.add((tx, ty))

# part 2
knots = [[0, 0] for _ in range(10)]
visited = set()
visited.add((0, 0))
for head_direction, steps in rows:
    steps = int(steps)
    for _ in range(steps):
        knots[0][0] += D[head_direction][0]
        knots[0][1] += D[head_direction][1]

        for i in range(1, 10):
            hx, hy = knots[i - 1]
            tx, ty = knots[i]

            if not touching(hx, hy, tx, ty):
                c = 0 if hx == tx else (hx - tx) // abs(hx - tx)
                d = 0 if hy == ty else (hy - ty) // abs(hy - ty)

                tx, ty = tx + c, ty + d

            knots[i] = [tx, ty]

        visited.add(tuple(knots[-1]))

print(len(visited))
