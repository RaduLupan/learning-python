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

poly2 = []
poly1 = [1, 2, 1]

result=multiply_basic(poly1, poly2)
print(result)
