'''
Problem: Write a recursive function that generates the first n elements of a Fibonacci sequence.
fibo(0) = 0
fibo(1) = 1
fibo(n) = fibo(n-1) + fibo(n-2)
'''
def fibonacci(n):
    pass

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
