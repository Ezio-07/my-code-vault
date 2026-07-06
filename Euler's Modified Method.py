# Euler's Modified Method
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
    yp = y + h * f(x, y)                          # predictor
    yc = y + (h / 2) * (f(x, y) + f(x + h, yp))   # corrector
    y = yc
    x = x + h
print("Approximate value of y =", ('%.6f' % y).rstrip('0').rstrip('.'))