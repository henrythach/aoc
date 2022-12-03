rows = [int(line.strip()) for line in open('./input.in', 'r')]

# part 1
# ans = 0
# for i in range(1, len(rows)):
#     if rows[i] > rows[i - 1]:
#         ans += 1
# print(ans)

# part 2
ans = 0
rows = [sum(rows[i-3:i]) for i in range(3, len(rows) + 1)]
for i in range(1, len(rows)):
    if rows[i] > rows[i - 1]:
        ans += 1
print(ans)
