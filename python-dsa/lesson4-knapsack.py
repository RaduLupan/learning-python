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
    index - a list of indices in the profits/weights lists for elements that if selected obtain the maximum profit for the given capacity.
    For the example inputs above, the output is [1,4] which means that the maximum profit is profits[1] + profits[4] = 3 + 10 = 13 and
    the used capacity is weights[1] + weights[4] = 1 + 11 = 12 < capacity.

'''

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
