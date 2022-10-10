'''
The following systematic strategy for solving problems will be used for the two problems below.

The method
1. State the problem clearly. Identify the input & output formats.
2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
3. Come up with a crrect solution for the problem. State it in plain English.
4. Implement the solution and test it using the example inputs. Fix bugs if any.
5. Analyze the algorithm's complexity and identify inefficiencies if any.
6. Apply the right technique to overcome the inefficiencies. Repeat steps 3-6. 

Problem1: You are given an array of numbers (non-negative). Find a continuous subarray of the list which adds up to a given sum.

'''


# 1. State the problem clearly. Identify the input & output formats.

# Input: arr - a list of positive numbers, target - a number representing the target sum.
arr1 = [1, 4, 7, 5, 10, 13]
target1 = 16

# Output: (i, j) - a tuple representing the start and end indices for the sub array in arr whose elements add up to target.
output1 = 1, 3 

