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
        
        already_sorted = True

        for j in range(n-i-1):
            
            print(f"i = {i},  j = {j}, array[j] = {array[j]}, array[j+1] = {array[j+1]}, array = {array}")
            if array[j] > array [j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] =  temp
                already_sorted = False

        if already_sorted:
            break
    
    return array

list=[1,2,3,4,5]
sorted_list=bubble_sort(list)
print(sorted_list)
