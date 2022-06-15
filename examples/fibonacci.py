'''
Problem: Write a recursive function that generates the first n elements of a Fibonacci sequence.
fibo(0) = 0
fibo(1) = 1
fibo(n) = fibo(n-1) + fibo(n-2)
'''
def fibonacci(n):
    '''
    Description: Calculates the n element of a Fibonacci sequence.
    '''
    if n > 1:
        f_n = fibonacci(n-1) + fibonacci(n-2)
    elif n == 1:
        f_n = 1
    elif n == 0:
        f_n = 0

    return f_n 

def generate_fibonacci_sequence(n):
    if n > 1:
        # Converts fibonacci(n) to a list with 1 element.
        f_n = [fibonacci(n)]
        
        # Recursive call.
        fibo = generate_fibonacci_sequence(n-1)
        
        # Extends the list for n-1 with the fibonacci(n).
        fibo.extend(f_n)
    elif n == 1:
        fibo = [0, 1]
    elif n == 0:
        fibo = [0]
    
    return fibo

def evaluate_test_case(function, test):
    '''
    Description: Compares actual output of a function with test case.
    Parameters:
    - function: the name of the function whose output is evaluated against test output.
    - test: test case in the form of a dictionary where test['input'] must match the arguments of function and test['output'] containes the tested output.
    TODO: Add measure of execution time for the function tested.
    '''    
    print(f"Input: {test['input']}")

    print (f"Expected Output: {test['output']}")
    
    result = function(test['input'])

    print(f"Actual Output: {result}")
    
    if result == test['output']:
        print("Test Result: PASSED\n")
    else:
        print ("Test Result: FAILED\n")

def evaluate_test_cases(function, tests):
    '''
    Description: Uses evaluate_test_case to compare actual output of a function with a series of test cases.
    Parameters:
    - function: the name of the function whose output is evaluated against test output.
    - tests: a list of test dictionaries where test['input'] must match the arguments of function and test['output'] containes the tested output.
    '''
    pass_count = 0
    fail_count = 0

    for test in tests:
        print(f"TEST#: {tests.index(test)}")
        
        print(f"Input: {test['input']}")

        print (f"Expected Output: {test['output']}")
    
        result = function(test['input'])

        print(f"Actual Output: {result}")   
        
        if result == test['output']:
            print("Test Result: PASSED\n")
            pass_count += 1
        else:
            print ("Test Result: FAILED\n")
            fail_count += 1
    
    print(f"SUMMARY\n TOTAL: {len(tests)}, PASSED: {pass_count}, FAILED: {fail_count}")

test = {
    'input': 0,
    'output': [0] 
}

test0=test

test1 = {
    'input': 1,
    'output': [0, 1]
}

test2 = {
    'input': 2,
    'output': [0, 1, 1]
}

test3 = {
    'input': 3,
    'output': [0, 1, 1, 2]
}

test4 = {
    'input': 4,
    'output': [0, 1, 1, 2, 3]
}

test5 = {
    'input': 5,
    'output': [0, 1, 1, 2, 3, 5]
}

test6 = {
    'input': 6,
    'output': [0, 1, 1, 2, 3, 5, 8]
}

test7 = {
    'input': 7,
    'output': [0, 1, 1, 2, 3, 5, 8, 13]
}

test8 = {
    'input': 8,
    'output': [0, 1, 1, 2, 3, 5, 8, 13, 21]
}

test9 = {
    'input': 9,
    'output': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9]

f=fibonacci(31)
print(f)

fibo=generate_fibonacci_sequence(15)
print(fibo)

# Evaluate generate_fibonacci_sequence function with one test.
# evaluate_test_case(function=generate_fibonacci_sequence, test=test4)

# Evaluate generate_fibonacci_sequence function with all tests.
evaluate_test_cases(function=generate_fibonacci_sequence, tests=tests)
