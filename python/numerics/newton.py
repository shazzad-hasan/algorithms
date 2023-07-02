def newton(f, dfdx, x, tol):
    f_val = f(x)
    count = 0
    while abs(f_val) > tol and count < 50:
        try:
            x = x - float(f_val)/dfdx(x) 
            f_val = f(x)
            count += 1
        except ZeroDivisionError:
            print("Zero division error!")
        
        print(f"i = {count}, x = {x}")

    return x, count 

def main():
# ---- test 1 ------
    def f(x):
        return x**2 - 9

    def dfdx(x):
        return 2*x

    tol = 1.0e-5
    sol, iter = newton(f, dfdx, 100, tol)
    print(sol)

    #  --- test 2 -----
    def f(x):
        return x**3 + x - 1

    def dfdx(x):
        return 3*x**2 + 1

    tol = 1.0e-5
    sol, iter = newton(f, dfdx, 10, tol)
    print(sol)

if __name__=="__main__":
    main()