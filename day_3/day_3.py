from string import ascii_letters

# { 'a': 1, 'b': 2, ... 'Y': 51, 'Z': 52 }
PRIORITY = {char: index + 1 for index, char in enumerate(ascii_letters)}

rows = [line.strip() for line in open('./input.txt')]

# part 1
# results = []
# for row in rows:
#     first_half = row[:len(row) // 2]
#     second_half = row[len(row) // 2:]
#     results.append(*set(first_half) & set(second_half))
# print(sum(PRIORITY[result] for result in results))


# part 2
results = []
for x in range(0, len(rows), 3):
    group_sets = [set(a) for a in rows[x:x + 3]]
    results.append(*set.intersection(*group_sets))
print(sum(PRIORITY[result] for result in results))
