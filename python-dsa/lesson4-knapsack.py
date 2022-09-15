'''
Modified Solution for the Knapsack Problem - Return the list of elements whose profits make up the maximum profit.

Originally the Knapsack problem statement was:
Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing 
no more than w.

Write a modified version of the max_profit function that returns the list of elements selected to maximize profit. 

Inputs:
    profits - list of numbers representing the profits.
    Example: [5, 3, 7, 2, 10]
    weights - list of numbers representing the weights (the two lists have the same length).
    Example: [7, 1, 10, 4, 11]
    capacity - a number representing the given capacity of the Knapsack.
    Example: 15.

Outputs:
    indices - a list of positions in the profits/weights lists for elements that if selected obtain the maximum profit for the given capacity.
    For the example inputs above, the output is [1,4] which means that the maximum profit is profits[1] + profits[4] = 3 + 10 = 13 and
    the used capacity is weights[1] + weights[4] = 1 + 11 = 12 < capacity.

'''
def max_profit_recursive(profits, weights, capacity, idx=0):
    '''
    Description: Returns the list of indices for elements in profits list that maximize the profit while staying within given weight (capacity).
    '''
    
    indices = []

    # Check if the profits/weights lists are exhausted.
    if idx == len(profits):
        return []
    
    # Check if the current element's weight is bigger than the capacity.
    elif weights[idx] > capacity:
        return max_profit_recursive(profits, weights, capacity, idx+1)
    
    # If the current element fits into the capacity, compute the two subproblems: either pick the element or don't and return the maximum. 
    else:
        # We pick the current element.
        indices.append(idx)
        option1 =  indices + max_profit_recursive(profits, weights, capacity-weights[idx], idx+1)
        option2 = max_profit_recursive(profits, weights, capacity, idx+1)

        # Compute the profit for the two options (list of indices) and return the list with greater profit as the solution.
        profit1, profit2 = 0, 0
        
        for i in option1:
            profit1 += profits[i]
        for i in option2:
            profit2 += profits[i]
        
        if profit1 > profit2:
            return option1
        else:
            return option2

# Test cases.

# General case 1.
test0 = {
    'input': {
        'profits': [5, 3, 7, 2, 10],
        'weights': [7, 1, 10, 4, 11],
        'capacity': 15
    },
    'output': [1, 4]
}

# General case 2.
test1 = {
    'input': {
        'profits': [15, 30, 45, 12, 17, 25],
        'weights': [13, 27, 41, 10, 11, 19],
        'capacity': 80
    },
    'output': [0, 1, 3, 4, 5]
}

# All weights are larger than the capacity.
test2 = {
    'input': {
        'profits': [10, 20, 30, 40, 50, 60],
        'weights': [15, 25, 35, 45, 55, 65],
        'capacity': 10
    },
    'output': []
}

# All weights fit into the capacity.
test3 = {
    'input': {
        'profits': [17, 302, 250, 180, 78, 13],
        'weights': [12, 185, 110, 90, 45, 9],
        'capacity': 500
    },
    'output': [0, 1, 2, 3, 4, 5]
}

# Only one element is selected.
test4 = {
    'input': {
        'profits': [7, 12, 5, 4, 2],
        'weights': [14, 25, 18, 7, 5],
        'capacity': 5
    },
    'output': [4]
}

tests = [test0, test1, test2, test3, test4]

# Evaluate one test case.
import dsa
dsa.evaluate_test_case(max_profit_recursive, test0)

# Evaluate all cases.
dsa.evaluate_test_cases(max_profit_recursive, tests)
