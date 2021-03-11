import numpy as np

G = 6.674e-11
M = 1.989e30
m = 5.972e24
R = 1.496e11
omega = 1.991e-7

def func1(r):
    """Subtracting first and second term"""
    t1 = G * M / r**2
    t2 = G * m / ((R-r)**2)
    t3 = omega**2 * r
    return t1 - t2 - t3
    
def fprime1(r):
    """Returns derivative of first function"""
    t1 = (-2 * G * M) / r**3
    t2 = (2 * G * M) / (R - r)**3
    t3 = omega**2
    return t1 - t2 - t3

def func2(r):
    """Adding first and second term"""
    t1 = G * M / r**2
    t2 = G * m / ((R-r)**2)
    t3 = omega**2 * r
    return t1 + t2 - t3

def fprime2(r):
    """Returns derivative of second function"""
    t1 = (-2 * G * M) / r**3
    t2 = (2 * G * M) / (R - r)**3
    t3 = omega**2
    return t1 + t2 - t3
    
def newtonsmethod(func = None, deriv = None, firstguess = None, maxiter = 50):
    guess = firstguess
    for i in range(maxiter):
        guess = guess - func(guess) / deriv(guess)
    return guess
    
def secant(func = None, x1 = None, x2 = None, maxiter = 50):
    for i in range(maxiter):
        t1 = x2 - func(x2)
        numer = (x2 - x1)
        deno = func(x2) - func(x1)
        x3 = x2 - (func(x2) * ((x2 - x1)) / (func(x2) - func(x1)))
        if deno <= 0:
            x1 = x2
            x2 = x3
        else:
            x2 = x1
            x1 = x3
    return x3
    
if __name__ == "__main__":
    
    # Solving Lagrange points 1 and 2 using Newtons method
    L1newtons = newtonsmethod(func = func1, deriv = fprime1, firstguess = 1.6e11)
    print('Lagrange point for L1 using Newtons method:', L1newtons)
    
    L2newtons = newtonsmethod(func = func2, deriv = fprime2, firstguess = 1.6e11)
    print('Lagrange point for L2 using Newtons method:', L2newtons)
    
    print('\n')

    # Solving Lagrange points for 1 and 2 using Secant method
    L1secant = secant(func = func1, x1 = 1e6, x2 = 1.9e10)
    print('Lagrange point for L1 using secant:', L1secant)
    
    L2secant = secant(func = func2, x1 = 1e6, x2 = 1.9e10)
    print('Lagrange point for L2 using secant:', L2secant)
