from collections import deque

lines = [row.strip() for row in open('input.txt', 'r')]
R = len(lines)
C = len(lines[0])
G = [[0 for _ in range(C)] for _ in range(R)]
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for row in range(R):
    for col in range(C):
        if lines[row][col] == 'S':
            G[row][col] = 1
        elif lines[row][col] == 'E':
            G[row][col] = 26
        else:
            G[row][col] = ord(lines[row][col]) - ord('a') + 1


def bfs():
    Q = deque()

    # find the starting point
    for r in range(R):
        for c in range(C):
            # part 1
            # if lines[r][c] == 'S':
            #     Q.append(((r, c), 0))

            # part 2
            if G[r][c] == 1:
                Q.append(((r, c), 0))

    seen = set()
    while Q:
        (r, c), d = Q.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))
        if G[r][c] == 26:
            print(d)
            return

        for dr, dc in DIRECTIONS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] <= G[r][c] + 1:
                Q.append(((rr, cc), d + 1))


bfs()
