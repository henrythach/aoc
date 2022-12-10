lines = [line.strip().split() for line in open('input.txt', 'r')]
X = 1
C = 0
signals = {20, 60, 100, 140, 180, 220}
strength = 0
stuff = []
CRT = []


def cycle():
    global C, X
    CRT.append('#' if abs(X - (C % 40)) <= 1 else '.')
    C += 1
    if C in signals:
        stuff.append(C * X)


for index, line in enumerate(lines):
    command = line[0]
    if command == 'noop':
        cycle()
    elif command == 'addx':
        cycle()
        cycle()
        X += int(line[1])

print(f"part 1 = {sum(stuff)}")
print("part 2")
for i in range(0, 220, 40):
    print(''.join(CRT[i:i+40]))
