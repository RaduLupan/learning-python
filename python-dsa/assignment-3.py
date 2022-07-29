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

def substract(poly1, poly2):
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

    return (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    '''
    Description: Multiplies polynomial poly with x^n.
    '''
    return [0] * n + [poly]
    
def multiply_optimized(a, b):
    '''
    Description: Performs multiplication of two polynomials represented by lists, using an Divide-and-Conquer algorithm.
    '''
    # If one polynom is a constant multiply all coeficients of the other polynom with the constant.
    if len(a) == 1 and len(b) > 1:
        return [v * a[0] for v in b]
    elif len(b) == 1 and len(a) > 1:
        return [v * b[0] for v in a]
    else:
        (a0, a1), (b0, b1) = split(a, b)

        if len(a0) == 1 and len(a1) == 2 and len(b0) == 1 and len(b1) == 2:
            return [(a[0] * b[0]), (a[0] * b[1] + a[1] * b[0]), (a[0] * b[2] + a[1] * b[1] + a[2] * b[0]), (a[1] * b[2] + a[2] * b[1]), a[2] * b[2]]

        y = multiply_optimized(add(a0, a1), add(b0, b1))
        u = multiply_optimized(a0, b0)
        z = multiply_optimized(a1, b1)

        negative_u = [-v for v in u]
        negative_z = [-v for v in z]

        result = u + increase_exponent(add(add(y, negative_u), negative_z), (len(a)-1) // 2) + increase_exponent(z, len(a) - 1)

        return result

poly1 = [4, 2, 3]
poly2 = [1, 1, 1]

result=substract(poly1, poly2)
print(result)
