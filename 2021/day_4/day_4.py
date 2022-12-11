class Board:
    grid: list
    seen: set

    def __init__(self, grid):
        self.grid = [row.split() for row in grid.strip().split('\n')]
        self.seen = set()
        self.won = False

    def add_number(self, number):
        self.seen.add(number)

    def is_winner(self):
        if self.won:
            return True

        # row by row
        for row in self.grid:
            if all(cell in self.seen for cell in row):
                self.won = True
                return True

        # col by col
        for i in range(5):
            if all(self.grid[j][i] in self.seen for j in range(5)):
                self.won = True
                return True

        return False

    def get_unseen_numbers(self):
        return sum(int(item) for row in self.grid for item in row if item not in self.seen)


file = open('input.txt', 'r').read().split('\n\n')
numbers = file[0].strip().split(',')
boards = [Board(b) for b in file[1:]]

num_of_boards = len(boards)
for number in numbers:
    for index, board in enumerate(boards):
        if board.won:
            continue

        board.add_number(number)
        if board.is_winner():
            num_of_boards -= 1
            sum_of_numbers = board.get_unseen_numbers()

            if num_of_boards == len(boards) - 1:
                print(f"Part 1 = {sum_of_numbers * int(number)}")

            if num_of_boards == 0:
                print(f"Part 2 = {sum_of_numbers * int(number)}")
                exit()
