'''
Problem statement
    You are in charge of selecting a football (soccer) team from a large pool of players. Each player has a cost, and a rating. 
    You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there is no minimum or maximum team size.

General problem statement:
    Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing 
    no more than w.
'''

def max_profit(profits, weights, capacity, idx=0):
    '''
    Description: Computes the maximum profit of a list of elements with given profits and weights restricted to a given capacity.
    '''

    if idx == len(weights):
        return 0
    
    # Check if the current element exceeds capacity.
    elif weights[idx] > capacity:
        return max_profit(profits, weights, capacity, idx+1)
    
    # If the current element fits into capacity, then compute the max of the two options of adding and not adding the element.
    else:
        option1=max_profit(profits, weights, capacity, idx+1)
        option2=profits[idx] + max_profit(profits, weights, capacity-weights[idx], idx+1)
        return max(option1, option2)

# Test cases.

# General case 1.
test0 = {
    'input': {
        'profits': [5, 3, 7, 2, 10],
        'weights': [7, 1, 10, 4, 11],
        'capacity': 15
    },
    'output': 13
}

# General case 2.
test1 = {
    'input': {
        'profits': [15, 30, 45, 12, 17, 25],
        'weights': [13, 27, 41, 10, 11, 19],
        'capacity': 80
    },
    'output': 92
}

# All weights are larger than the capacity.
test2 = {
    'input': {
        'profits': [10, 20, 30, 40, 50, 60],
        'weights': [15, 25, 35, 45, 55, 65],
        'capacity': 10
    },
    'output': 0
}

# All weights fit into the capacity.
test3 = {
    'input': {
        'profits': [17, 302, 250, 180, 78, 13],
        'weights': [12, 185, 110, 90, 45, 9],
        'capacity': 500
    },
    'output': 840
}

# Only one element is selected.
test4 = {
    'input': {
        'profits': [7, 12, 5, 4, 2],
        'weights': [14, 25, 18, 7, 5],
        'capacity': 5
    },
    'output': 2
}

tests = [test0, test1, test2, test3, test4]

# Evaluate the first test case.
print(max_profit(**test4['input']))
