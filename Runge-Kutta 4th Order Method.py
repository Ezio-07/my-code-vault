# Runge-Kutta 4th Order Method
import math
equation = input("Enter dy/dx in terms of x and y: ")
def f(x, y):
    return eval(equation)
x0 = float(input("Enter initial value of x: "))
y0 = float(input("Enter initial value of y: "))
h = float(input("Enter step size h: "))
xn = float(input("Enter value of x at which y is required: "))
steps = int((xn - x0) / h)
x = x0
y = y0
for i in range(steps):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h
print("Approximate value of y =", ('%.6f' % y).rstrip('0').rstrip('.'))