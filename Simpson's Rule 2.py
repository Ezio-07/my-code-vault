# Simpson's 3/8th Rule
n = int(input("Enter number of intervals (multiple of 3): "))
if n % 3 != 0:
    print("Error: Simpson's 3/8 rule requires number of intervals to be a multiple of 3.")
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
    total = y[0] + y[n]
    for i in range(1, n):
        if i % 3 == 0:
            total += 2 * y[i]
        else:
            total += 3 * y[i]
    result = (3 * h / 8) * total
    print("Value of integration =", ('%.6f' % result).rstrip('0').rstrip('.'))