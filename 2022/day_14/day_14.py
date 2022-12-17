lines = [line.strip() for line in open('./input.txt', 'r')]
filled = set()
for line in lines:
    coords = []
    for coord in line.split(' -> '):
        x, y = map(int, coord.split(','))
        coords.append((x, y))

    for i in range(1, len(coords)):
        px, py = coords[i - 1]
        cx, cy = coords[i]

        # print(f"{(px, py)} -> {(cx, cy)}")

        if px != cx:
            for x in range(min(px, cx), max(px, cx) + 1):
                # print(f"Fill/ing in {(x, cy)}")
                filled.add((x, cy))

        if py != cy:
            for y in range(min(py, cy), max(py, cy) + 1):
                # print(f"Filling in {(cx, y)}")
                filled.add((cx, y))

# part 1
# bottom = max(f[1] for f in filled)
bottom = max(f[1] for f in filled)


def drip():
    x, y = 500, 0

    while y <= bottom:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        # part 1
        # filled.add((x, y))
        # print(f"Nice. {(x, y)}")
        # return True

        break

    return (x, y)


# part 1
# ans = 0
# while True:
#     if not drip():
#         break
#     ans += 1
# print(ans)


# part 2
ans = 0
while True:
    x, y = drip()
    filled.add((x, y))
    ans += 1
    # print(ans, x, y)
    if (x, y) == (500, 0):
        # print('yoooo')
        break
print(ans)
