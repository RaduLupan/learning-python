'''
Divide-n-Conquer Algorithms in Python

Problem 1:
Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials.
Example: 
The lists [2, 0, 5, 7] and [3, 4, 2] represent the polynomials 2 + 5*x**2 + 7*x**3 and 3 + 4*x + 2*x**2.
Their product is: 6 + 8*x + 19*x**2 + 41*x**3 + 38*x**4 + 14*x**5 
which is represented by the list [6, 8, 19, 41, 38, 14]
'''
def multiply_basic(poly1, poly2):
    '''
    Description: Performs multiplication of two polynomials represented by lists using the brute-force approach.
    '''
    # If either list is empty the result is an empty list.
    if poly1 == [] or poly2 == []:
        return []
    
    # If either list contains all zeros the result is an empty list.
    elif all([value == 0 for value in poly1]) or all([value == 0 for value in poly2]):
        return [] 
    else:
        # m and n are the degrees of the two polynomials respectively. 
        m, n = len(poly1)-1, len(poly2)-1
        
        # The result list will represent a polynomial with degree m+n which has a lenght of m+n+1.
        result = [0] * (m+n+1)

        # We calculate the coefficients of the result using the formula:
        # result[k] = sum(poly1[i]*poly2[k-i]) for 0 <= i <= k and 0 <= k <= (m+n)
        
        # Initialize index in the result list.
        k = 0

        # Iterate until the end of the result list.
        while k <= m+n:
            
            # Initialize the index on the poly1 list.
            i, sum = 0, 0
        
            # Iterate through all elements of poly1 list.
            while i <= m:
                
                # All coefficients corresponding to powers greater than n are zero so skip them.
                if k-i <= n:
                    sum += poly1[i] * poly2[k-i]
                
                print(f"k={k}, i={i}")
                
                # Increment the index on poly1 list only if less than k, otherwise skip since that coefficient would have been zero.
                if i < k:
                    i += 1
                else:
                    break
            result[k] = sum
            print(f"k={k}, result[k]={result[k]}")
            
            k += 1
        return result

def add(poly1, poly2):
    '''
    Description: Adds two polynomials represented by lists and returns a list representing the sum polynomial.
    '''

    # Creates a result list of lenght equal with the largest length.
    result = [0] * max(len(poly1), len(poly2))

    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def subtract(poly1, poly2):
    '''
    Description: Implements polynomial substraction.
    '''
    poly2 = [-v for v in poly2]

    return add(poly1, poly2)
def split(poly1, poly2):
    '''
    Description: Splits each polynomial into two smaller polynomials.
    '''
    mid = max(len(poly1), len(poly2)) // 2
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

    return (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    '''
    Description: Multiplies polynomial poly with x^n.
    '''
    return [0] * n + [poly]
    
def multiply_optimized(poly1, poly2):
    '''
    Description: Performs multiplication of two polynomials represented by lists, using an Divide-and-Conquer algorithm.
    TODO: Fix unsupported operand type(s) for +=: 'int' and 'list'
    '''
    # If either list is empty the result is an empty list.
    if poly1 == [] or poly2 == []:
        return []

    # If either list contains all zeros the result is an empty list.
    elif all([value == 0 for value in poly1]) or all([value == 0 for value in poly2]):
        return [] 

    # If one polynom is a constant multiply all coeficients of the other polynom with the constant.
    elif len(poly1) == 1:
        return [v * poly1[0] for v in poly2]
    
    elif len(poly2) == 1:
        return [v * poly2[0] for v in poly1]
    
    else:
        print(f"multiply_optimized({poly1},{poly2})")

        n =  max(len(poly1), len(poly2))
        n = n if n % 2 == 0 else n-1

        a, b = split(poly1, poly2) 
            
        u = multiply_optimized(a[0], b[0])
        z = multiply_optimized(a[1], b[1])
        
        y = multiply_optimized(add(a[0], a[1]), add(b[0], b[1]))
                   
        y = subtract(y, add(u, z))
        y = increase_exponent(y, n//2)
            
        z = increase_exponent(z, n)
        result = add((add(u, z), y))
        return result

    
poly1 = [1, 2, 3, 1]
poly2 = [2, 1, 1, 2]

result=multiply_optimized(poly1, poly2)
#result1 = add(poly1, poly2)
#result2 = subtract(poly1, poly2)
print(result)
