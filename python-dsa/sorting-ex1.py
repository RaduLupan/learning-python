'''
Implements various sorting algorithms.
'''

def bubble_sort(array):
    '''
    Description: Sorts a list using the Bubble Sort algorithm.
    Algorithm:
    1. Make multiple passes through an array.
    2. Compare elements one by one and swap adjacent elements that are out of order.
    3. Repeat steps 1-2 until there are no more swaps to be done which means the array is sorted in ascending order.
    '''

    n = len(array)

    for i in range(n):
        
        # Create a flag that will allow the function to terminate early if there is nothing left to sort.
        # This is just an optimization of the algorithm and is not required for a fully functional bubble sort implementation.
        already_sorted = True

        # With every array iteration the one by one comparisons go closer and closer to the left since the right end becomes sorted.
        for j in range(n-i-1):
            
            print(f"i = {i},  j = {j}, array[j] = {array[j]}, array[j+1] = {array[j+1]}, array = {array}")
            
            if array[j] > array [j+1]:
                # Swap elements.
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False

        if already_sorted:
            break
    
    return array

list=[5,4,3,2,1]
sorted_list=bubble_sort(list)
print(sorted_list)
