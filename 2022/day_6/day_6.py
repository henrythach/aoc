s = open('input.txt', 'r').read().strip()
c = 14
for i in range(c-1, len(s)):
    sequence = s[i-c:i]
    if len(set(sequence)) == c:
        print(i, sequence)
        break
