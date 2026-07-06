# Gauss Elimination Method
n = int(input("Enter number of variables: "))
a = []
print("Enter augmented matrix coefficients:")
for i in range(n):
    row = list(map(float, input().split()))
    if len(row) != n + 1:
        print(f"Error: Row {i+1} must contain {n+1} values (got {len(row)}).")
        exit()
    a.append(row)
# Forward Elimination
for i in range(n):
    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]
# Back Substitution
x = [0 for i in range(n)]
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
for i in range(n - 2, -1, -1):
    sum = 0
    for j in range(i + 1, n):
        sum = sum + a[i][j] * x[j]
    x[i] = (a[i][n] - sum) / a[i][i]
print("\nSolution:")
for i in range(n):
    val = ('%.6f' % x[i]).rstrip('0').rstrip('.')
    print(f"x{i+1} = {val}")