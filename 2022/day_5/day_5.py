# stacks = [
#     [],
#     [x for x in 'ZN'],
#     [x for x in 'MCD'],
#     [x for x in 'P'],
# ]

stacks = [
    [],
    [x for x in 'ZMPHR'],
    [x for x in 'PCJB'],
    [x for x in 'SNHGLCD'],
    [x for x in 'FTMDQSRL'],
    [x for x in 'FSPQBTZM'],
    [x for x in 'TFSZBG'],
    [x for x in 'NRV'],
    [x for x in 'PGLTDVCM'],
    [x for x in 'WQNJFML'],
]

rows = [line.strip() for line in open('input.txt')]
for row in rows:
    first, second = row.split(' from ')
    _, quantity = first.split(' ')
    quantity = int(quantity)
    src, dest = map(int, second.split(' to '))

    # part 1
    # stacks[src], stacks[dest] = stacks[src][0:-quantity], \
    #                             stacks[dest] + stacks[src][:-quantity - 1:-1]

    # part 2
    stacks[src], stacks[dest] = stacks[src][0:-quantity], \
        stacks[dest] + stacks[src][-quantity:]

print(''.join(list(stack[-1] for stack in stacks if len(stack) > 0)))
