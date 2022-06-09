'''
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
'''

def locate_card_linear_search(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        
        position += 1

    return -1

def locate_card_binary_search(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        result = test_location(cards=cards, query=query, mid=mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1

def test_location (cards, query, mid):
    mid_number = cards[mid]
    
    print("mid:", mid, ", mid_number:", mid_number)

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else: 
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def binary_search(lo,hi,condition):
    '''
    Description: Generic algorithm for binary search. The condition argument is a function that determines whether the answer lies before, after or at a given position.
    Use in conjunction with locate_card function.
    '''
    pass

def locate_card(cards, query):
    '''
    Description: Uses generic binary search algorithm to locate the index of a card (query) in a list (cards).
    Use in conjunction with binary_search function.
    '''
    pass

def evaluate_test_case(locate_card, test):
    print(f'Test {test}')
    
    result = locate_card(**test['input'])
    
    if result == test['output']:
        print('PASS')
    else:
        print ('FAIL')

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

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

print(len(tests))
print(tests[7])
print(locate_card_binary_search(**tests[7]['input']))

evaluate_test_case(locate_card=locate_card_binary_search, test=tests[7])
