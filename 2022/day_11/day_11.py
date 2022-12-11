from collections import deque
from math import prod


class Monkey:
    items: deque
    operator: str
    operand: str
    divisible: int
    monkey_true: int
    monkey_false: int
    inspection_count: int
    divisor: int

    def __init__(self, text: list, d: int):
        self.items = deque(map(int, text[1].split('Starting items: ')[-1].split(', ')))
        self.operator, self.operand = text[2].split('Operation: new = old ')[1].split()
        self.divisible = int(text[3].split('divisible by ')[-1])
        self.monkey_true = int(text[4].split('If true: throw to monkey ')[-1])
        self.monkey_false = int(text[5].split('If false: throw to monkey ')[-1])
        self.inspection_count = 0
        self.divisor = d

    def receive(self, the_item: int):
        self.items.append(the_item)

    def take_turn(self, modulo: int):
        while len(self.items):
            curr_item = self.items.popleft()
            worry_level = self.determine_worry_level(curr_item) % modulo
            self.inspection_count += 1
            yield self.test(worry_level)

    def determine_worry_level(self, the_item: int) -> int:
        operand = int(self.operand) if self.operand.isnumeric() else the_item
        value = 0
        if self.operator == '*':
            value = the_item * operand
        elif self.operator == '+':
            value = the_item + operand
        return value

    def test(self, worry_level: int):
        curr_worry_level = worry_level // self.divisor
        to_monkey = self.monkey_true if curr_worry_level % self.divisible == 0 else self.monkey_false
        return to_monkey, curr_worry_level


divisor = 1
rounds = 10000
monkeys = [Monkey(row.split('\n'), divisor) for row in open('input.txt', 'r').read().split('\n\n')]
gcm = prod(monkey.divisible for monkey in monkeys)
for _ in range(rounds):
    for src_monkey_index, monkey in enumerate(monkeys):
        for dest_monkey_index, item in monkey.take_turn(gcm):
            monkeys[dest_monkey_index].receive(item)

for index, monkey in enumerate(monkeys):
    print(f"Monkey {index} inspected items {monkey.inspection_count} times")

inspected = sorted([m.inspection_count for m in monkeys], reverse=True)
print(inspected[0] * inspected[1])
