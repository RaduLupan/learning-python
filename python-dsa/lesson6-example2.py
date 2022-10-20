'''
The following systematic strategy for solving problems will be used for the two problems below.

The method
1. State the problem clearly. Identify the input & output formats.
2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using the example inputs. Fix bugs if any.
5. Analyze the algorithm's complexity and identify inefficiencies if any.
6. Apply the right technique to overcome the inefficiencies. Repeat steps 3-6. 

Problem2: Given two strings A and B, find the minimum number of steps required to convert A to B. You have the following 3 operations permitted on a word:
-> Insert a character
-> Delete a character
-> Replace a character
Eeach operation is counted as 1 step.
'''

# 1. State the problem clearly. Identify the input & output formats.
# Input: str1, str2 are the two strings to process.
# Output: an integer representing the minimum number of operations (insert/delete/replace) applied to str1 string in order to convert it str2 string.
# Example:
# str1 = 'intention'
# str2 = 'execution'
# output = 5

def min_steps(str1, str2, idx1=0, idx2=0):
    
    # idx1 and idx2 are tracking the indices of current characters in str1 and str2 respectively.

    print(f"min_steps({str1[idx1:]},{str2[idx2:]})")

    # If we reached the end of str1 return the remaining number of characters in str2.
    if idx1 == len(str1): 
        return len(str2) - idx2
    # If we reached the end of str2 return the remaining number of characters in str1.
    elif idx2 == len(str2):
        return len(str1) - idx1
    # The first characters are equal.
    elif str1[idx1] == str2[idx2]:
        return min_steps(str1, str2, idx1+1, idx2+1)
    else:
        delete = 1 + min_steps(str1, str2, idx1+1, idx2)
        replace = 1 + min_steps(str1, str2, idx1+1, idx2+1)
        insert = 1 + min_steps(str1, str2, idx1, idx2+1)
        return min(delete, replace, insert)

# 2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
# 2.1 General case.
test0 = {
    'input': {
        'str1': 'intention',
        'str2': 'execution'
    },
    'output': 5
}

# 2.2 No change required (str1 and str2 are equal).
test1 = {
    'input': {
        'str1': 'algorithm',
        'str2': 'algorithm'
    },
    'output': 0
}

# 2.3 All characters in str1 need to be changed.
test2 = {
    'input': {
        'str1': 'morning',
        'str2': 'summer'
    },
    'output': 7
}

# 2.4 The two strings have equal length.
test3 = {
    'input': {
        'str1': 'fog',
        'str2': 'dog'
    },
    'output': 1
}

# 2.5 The two strungs have unequal length.
test4 = {
    'input': {
        'str1': 'nation',
        'str2': 'equation'
    },
    'output': 3
}

# 2.6 One of the strings is empty.
test5 = {
    'input': {
        'str1': '',
        'str2': 'reality'
    },
    'output': 7
}

# 2.7 Only one type of operation is required: one deletion, or one substitution or one insertion.
test6 = {
    'input': {
        'str1': 'fog',
        'str2': 'frog'
    },
    'output': 1
}

tests = [test0, test1, test2, test3, test4, test5, test6]

# 3. Recursive solution - brute force.
'''
If the first characters are equal then ignore them and recursively solve for the remaining strings.
If the first caracters are not equal:
    1. Either apply DELETE operation
       the solution is 1 + recursively solving for remaining of str1 and entire str2. 
    2. Or apply REPLACE operation
       the solution is 1 + recursively solving for remaining of str1 and remaining of str2.
    3. Or apply INSERT operation
       the solution is 1 + recursively solving for entire str1 and remaining str2.
'''

import dsa

# dsa.evaluate_test_case(min_steps, test6)
# dsa.evaluate_test_cases(min_steps, tests)

# 5. Analyze the algorithm's complexity and identify inefficiencies if any.
# The time complexity for the brute force solution is O(3^(m+n)) where m=len(str1) and n=len(str2). 
# There are a lot of repetitive calls. For m+n=20 there will be over 3.4 bilion recursive calls!!

# 6. Apply the right technique to overcome the inefficiencies.
# One way to overcome the inefficiencies is to use a technique called memoization where the results are stored in a dictionary to avoid repetitive calls.

def min_steps_memo(str1, str2):
    '''
    Uses memoization technique to avoid repetitive calls.
    '''
    
    # Dictionary to store intermediate results.
    memo = {}

    def recurse(idx1, idx2):
        key = (idx1, idx2)

        if key in memo:
            return memo[key]
        elif idx1 == len(str1):
            memo[key] = len(str2) - idx2
        elif idx2 == len(str2):
            memo[key] = len(str1) - idx1
        elif str1[idx1] == str2[idx2]:
            memo[key] = recurse(idx1+1, idx2+1)
        else:
            delete = 1 + recurse(idx1+1, idx2)
            replace = 1 + recurse(idx1+1, idx2+1)
            insert = 1 + recurse(idx1, idx2+1)
            memo[key] = min(delete, replace, insert)
        
        return memo[key]

    return recurse(0, 0) 

dsa.evaluate_test_case(min_steps_memo, test0)

dsa.evaluate_test_cases(min_steps_memo, tests)
