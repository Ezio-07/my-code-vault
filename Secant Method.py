# Secant Method
import math
equation = input("Enter the equation in x: ")
def f(x):
    return eval(equation)
x1 = float(input("Enter first guess: "))
x2 = float(input("Enter second guess: "))
tolerance = float(input("Enter tolerance value: "))
iterations = 0
maxiterations = 200
def end():
    print("Root =", ('%.6f' % x3).rstrip('0').rstrip('.'))
    print("Number of iterations =", ('%.6f' % iterations).rstrip('0').rstrip('.'))
if f(x1) == 0:
    x3 = x1
    end()
elif f(x2) == 0:
    x3 = x2
    end()
if f(x2) - f(x1) == 0:
    print("Method failed to converge. Choose different points.")
while abs(x1 - x2) > tolerance:
    x3 = ((x1 * f(x2)) - (x2 *f(x1))) / (f(x2) - f(x1))
    x1 = x2
    x2 = x3
    iterations += 1
    if iterations == maxiterations:
        print("Method failed to converge. Maximum iterations reached.")
end()