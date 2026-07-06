# Newton-Raphson Method
import math
equation = input("Enter the equation in x: ")
derivative = input("Enter derivative of equation: ")
def f(x):
    return eval(equation)
def df(x):
    return eval(derivative)
x0 = float(input("Enter initial guess: "))
tolerance = float(input("Enter tolerance value: "))
iterations = 0
maxiterations = 200
def end():
    print("Root =", ('%.6f' % x1).rstrip('0').rstrip('.'))
    print("Number of iterations =", ('%.6f' % iterations).rstrip('0').rstrip('.'))
if f(x0) == 0:
    x1 = x0
    end()
elif df(x0) == 0:
    print("Invalid Interval")
while abs(f(x0)) > tolerance:
    x1 = x0 - f(x0) / df(x0)
    x0 = x1
    iterations += 1
    if iterations == maxiterations:
        print("Maximum iterations reached. Method failed to converge.")
end()