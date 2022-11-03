def sign(x):
    if x < 0: return -1 
    elif x > 0: return 1 
    else: return 0

def bisect(f, a, b, tol):
    """ Bisection Method
    Input: function f, interval [a, b], tolerance 
    Output: Returns approximate sol'n 
    """
    fa, fb = f(a), f(b)
    if sign(fa) * sign(fb) >= 0:
        print(f"f(a)*f(b) < 0 not satisfied!")
        return 
    else:
        while (b-a)/2 > tol:
            c = (a+b)/2
            fc = f(c)
            if fc == 0: return c 
            elif sign(fc)*sign(fa) < 0:
                b = c 
                fb = fc 
            else:
                a = c 
                fa = fc 
        return (a+b)/2

from math import cos 
def f(x):
    return cos(x) - x 
tol = 1.0e-3
print(bisect(f, 0, 1, tol))

tol = 1.0e-5
def g(x):
    return x**3+x-1
print(bisect(g, 1, 2, tol))
print(bisect(g, 0, 1, tol))

