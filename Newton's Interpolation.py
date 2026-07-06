# Newton's Forward/Backward Interpolation
n = int(input("Enter number of data points: "))
x = []
y = []
print("Enter x and y values:")
for i in range(n):
    xi, yi = map(float, input().split())
    x.append(xi)
    y.append(yi)
value = float(input("\nEnter value of x: "))
equal_spacing = True
h = x[1] - x[0]
for i in range(1, n - 1):
    if abs((x[i+1] - x[i]) - h) > 1e-9:
        equal_spacing = False
        break
if not equal_spacing:
    print("\nError: Intervals are not equally spaced. Newton's interpolation cannot be applied.")
    exit()
diff = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    diff[i][0] = y[i]
for j in range(1, n):
    for i in range(n - j):
        diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
def format_number(num, width=12):
    s = ('%.6f' % num).rstrip('0').rstrip('.')
    return f"{s:>{width}}"
print("\nDifference Table:")
headers = ["x", "y"] + [f"Δ^{j}y" for j in range(1, n)]
for hname in headers:
    print(f"{hname:>12}", end="")
print()
for i in range(n):
    print(format_number(x[i]), end="")
    for j in range(n - i):
        print(format_number(diff[i][j]), end="")
    print()
if abs(value - x[0]) <= abs(value - x[-1]):
    # Forward interpolation
    print("\nUsing Forward Interpolation")
    p = (value - x[0]) / h
    result = y[0]
    p_term = 1
    factorial = 1
    for i in range(1, n):
        p_term *= (p - i + 1)
        factorial *= i
        result += (p_term * diff[0][i]) / factorial
else:
    # Backward interpolation
    print("\nUsing Backward Interpolation")
    p = (value - x[-1]) / h
    result = y[-1]
    p_term = 1
    factorial = 1
    for i in range(1, n):
        p_term *= (p + i - 1)
        factorial *= i
        result += (p_term * diff[n - i - 1][i]) / factorial
print("Interpolated value =", ('%.6f' % result).rstrip('0').rstrip('.'))