'''
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
'''

def locate_card(cards, query):
    pass

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

locate_card(**test['input']) == test['output']

tests=[]

# Create tests for some edge cases.

# query is somewhere in the middle of cards.
tests.append(test)

# query is the first element.
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element.
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains only one element which is query.
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards does not contain query.
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty.
tests.append({
    'input': {
        'cards': [],
        'query' : 4
    },
    'output': -1
})

# numbers can repeat in cards.
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

#query can occure multiple times.
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)
