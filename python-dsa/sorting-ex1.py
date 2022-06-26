'''
Implements various sorting algorithms.
'''

def bubble_sort(array):
    '''
    Description: Sorts a list using the Bubble Sort algorithm.
    Algorithm:
    1. Iterate through the items in the array multiple times, at each iteration compare the current item with the adjacent one.
    2. If the current item is greater than the adjacent one swap their places so that the greater item moves towards its correct position in the array.
    3. Repeat step 2 for until the second last item in the array.
    4. Repeat steps 1-3 until there are no more swaps to be done which means the array is sorted in ascending order.
    '''
