from collections import Counter

rows = [line.strip() for line in open('./input.in', 'r')]
gamma, epsilon = 0, 0
for i, x in enumerate(zip(*rows)):
    C = Counter(x)
    position = len(rows[0]) - i - 1
    gamma |= int(C['0'] < C['1']) << position
    epsilon |= int(C['0'] > C['1']) << position
print(f"part 1 = {gamma * epsilon}")

num_bits = len(rows[0])
oxygen = rows.copy()
co2 = rows.copy()
for position in range(num_bits, 0, -1):
    if len(oxygen) > 1:
        oxy_count = Counter(list(zip(*oxygen))[num_bits - position])
        oxy_common = '1' if oxy_count['1'] >= oxy_count['0'] else '0'
        oxygen = [x for x in oxygen if x[num_bits - position] == oxy_common]

    if len(co2) > 1:
        co2_count = Counter(list(zip(*co2))[num_bits - position])
        co2_common = '0' if co2_count['0'] <= co2_count['1'] else '1'
        co2 = [x for x in co2 if x[num_bits - position] == co2_common]

oxy_rating = int(oxygen[0], 2)
co2_rating = int(co2[0], 2)
print(f"part 2 = {oxy_rating * co2_rating}")
