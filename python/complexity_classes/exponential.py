def fibonacci(n):
    """ 
    Take in a positive integer and return nth fibonacci number 
    
    Complexity: O(2^n)
    
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)