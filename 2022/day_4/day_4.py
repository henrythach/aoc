pairs = [line.strip().split(',') for line in open('input.txt', 'r')]

ans = 0

for pair in pairs:
    group_1, group_2 = map(lambda x: x.split('-'), pair)
    group_1, group_2 = list(map(int, group_1)), list(map(int, group_2))

    min_1, max_1 = min(group_1), max(group_1)
    min_2, max_2 = min(group_2), max(group_2)

    # part 1
    # if (min_1 <= min_2 and max_1 >= max_2) or \
    #    (min_2 <= min_1 and max_2 >= max_1):
    #     ans += 1

    # part 2
    if (min_2 <= min_1 <= max_2) or (min_2 <= max_1 <= max_2) or \
       (min_1 <= min_2 <= max_1) or (min_1 <= max_2 <= max_1):
        ans += 1

print(ans)
