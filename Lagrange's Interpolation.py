# Lagrange's Interpolation
n = int(input("Enter number of data points: "))
x = []
y = []
print("Enter x and y values:")
for i in range(n):
    xi, yi = map(float, input().split())
    x.append(xi)
    y.append(yi)
choice = int(input("Enter 1 for y corresponding to x\nEnter 2 for x corresponding to y\n"))
# Direct Interpolation
if choice == 1:
    value = float(input("Enter value of x: "))
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (value - x[j]) / (x[i] - x[j])
        result = result + term
    print("Interpolated value of y =", ('%.6f' % result).rstrip('0').rstrip('.'))
# Inverse Interpolation
elif choice == 2:
    value = float(input("Enter value of y: "))
    result = 0
    for i in range(n):
        term = x[i]
        for j in range(n):
            if i != j:
                term = term * (value - y[j]) / (y[i] - y[j])
        result = result + term
    print("Interpolated value of x =", ('%.6f' % result).rstrip('0').rstrip('.'))
else:
    print("Invalid Choice")