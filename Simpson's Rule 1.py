# Simpson's 1/3rd Rule
n = int(input("Enter number of intervals (even): "))
if n % 2 != 0:
    print("Error: Simpson's 1/3 rule requires an even number of intervals.")
x = []
y = []
print("Enter x and y values:")
for i in range(n + 1):
    xi, yi = map(float, input().split())
    x.append(xi)
    y.append(yi)
equal_spacing = True
h = x[1] - x[0]
for i in range(1, n):
    if abs((x[i+1] - x[i]) - h) > 1e-9:  # tolerance for floating-point
        equal_spacing = False
        break
if not equal_spacing:
    print("\nError: Intervals are not equally spaced. Trapezoidal rule cannot be applied.")
else:
    sum = y[0] + y[n]
    for i in range(1, n):
        if i % 2 == 0:
            sum = sum + 2 * y[i]
        else:
            sum = sum + 4 * y[i]
    result = (h / 3) * sum
    print("Value of integration =", ('%.6f' % result).rstrip('0').rstrip('.'))