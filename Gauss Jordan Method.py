# Gauss Jordan Method
n = int(input("Enter number of variables: "))
a = []
print("Enter augmented matrix coefficients:")
for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)
for i in range(n):
    pivot = a[i][i]
    for j in range(n + 1):
        a[i][j] = a[i][j] / pivot
    for k in range(n):
        if k != i:
            factor = a[k][i]
            for j in range(n + 1):
                a[k][j] = a[k][j] - factor * a[i][j]
print("Solution:")
for i in range(n):
    val = ('%.6f' % a[i][n]).rstrip('0').rstrip('.')
    print(f"x{i+1} = {val}")