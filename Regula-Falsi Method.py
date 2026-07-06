# Regula-Falsi Method
import math
equation = input("Enter the equation in x: ")
def f(x):
    return eval(equation)
x1 = float(input("Enter first guess: "))
x2 = float(input("Enter second guess: "))
tolerance = float(input("Enter tolerance value: "))
iterations = 0
def end():
    print("Root =", ('%.6f' % root).rstrip('0').rstrip('.'))
    print("Number of iterations =", ('%.6f' % iterations).rstrip('0').rstrip('.'))
if f(x1) == 0:
    root = x1
    end()
elif f(x2) == 0:
    root = x2
    end()
elif f(x1) * f(x2) >= 0:
    print("Invalid Interval")
else:
    while abs(x1 - x2) > tolerance:
        x0 = ((x1 * f(x2)) - (x2 * f(x1))) / (f(x2) - f(x1))
        iterations += 1
        if f(x0) == 0:
            break
        elif f(x1) * f(x0) < 0:
            x2 = x0
        else:
            x1 = x0
    root = x0
    end()