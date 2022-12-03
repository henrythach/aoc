EXTRA_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
PERMUTATIONS = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}
STRATEGY = {
    'X': -1,  # to lose
    'Y': 0,  # to tie
    'Z': 1  # to tie
}


def get_score(first_column, second_column):
    score = PERMUTATIONS[(first_column, second_column)]
    extra = EXTRA_POINTS[second_column]
    return score + extra


def get_score_2(opponent, second_column):
    opponent_ordinal = ord(opponent) - ord('A')
    diff = STRATEGY[second_column]
    my_answer = 'XYZ'[(opponent_ordinal + diff) % 3]
    return get_score(opponent, my_answer)


print(sum(get_score_2(*line.strip().split(' '))
          for line in open('./input.txt')))
