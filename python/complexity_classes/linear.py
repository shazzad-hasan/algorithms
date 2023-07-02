def factorial(n):
    """ 
    Takes in a number n, assume n>0 and return n!
    
    Complexity: O(n)
    
    """
    # using loop
    # prod = 1
    # for i in range(1, n+1):
    #     prod *= i
    # return prod 

    # recursive version
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)