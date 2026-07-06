# Runge-Kutta 2nd Order Method
import math
equation = input("Enter dy/dx in terms of x and y: ")
def f(x, y):
    return eval(equation)
x = float(input("Enter initial value of x: "))
y = float(input("Enter initial value of y: "))
h = float(input("Enter step size h: "))
xn = float(input("Enter value of x at which y is required: "))
steps = int((xn - x) / h)
for i in range(steps):
    k1 = h * f(x, y)
    k2 = h * f(x + h, y + k1)
    y = y + (k1 + k2) / 2
    x = x + h
print("Approximate value of y =", ('%.6f' % y).rstrip('0').rstrip('.'))