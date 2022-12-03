TOP_K = 3

results = []

with open('./day_1/input.txt', 'r') as f:
    current_sum = 0
    for row in f:
        if len(row.strip()) == 0:
            results.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(row.strip())

print(sum(sorted(results, reverse=True)[:TOP_K]))
