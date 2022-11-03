def fib(n, memo = {}):
    """
    Assumes n is an integer, n >= 0,
    memo (momoization) used only be recursive calls,
    Returns fibonnaci of n.
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result 
        return result 

for i in range(121):
    print(f"fib({i}) = {fib(i)}")