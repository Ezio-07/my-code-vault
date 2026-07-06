# Gauss-Seidel Method
n = int(input("Enter number of variables: "))
a = []
print("Enter augmented matrix coefficients:")
for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)
coeff = [row[:n] for row in a]
b = [row[n] for row in a]
print("Enter initial guesses:")
x = list(map(float, input().split()))
tolerance = float(input("Enter tolerance value: "))
def is_diagonally_dominant(matrix, n):
    for i in range(n):
        diag = abs(matrix[i][i])
        off_diag_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if diag < off_diag_sum:
            return False
    return True
if is_diagonally_dominant(coeff, n):
    print("\nMatrix is diagonally dominant")
else:
    print("\nWarning: Matrix is NOT diagonally dominant")
    print("Gauss-Seidel method will not converge for this system.")
    exit()
iteration_count = 0
while True:
    iteration_count += 1
    max_error = 0
    for i in range(n):
        old = x[i]
        total = 0
        for j in range(n):
            if i != j:
                total += coeff[i][j] * x[j]
        x[i] = (b[i] - total) / coeff[i][i]
        if abs(x[i] - old) > max_error:
            max_error = abs(x[i] - old)
    if max_error < tolerance:
        break
print(f"\nConverged in {iteration_count} iterations.")
print("\nSolution:")
for i in range(n):
    val = x[i]
    if abs(val - round(val)) < tolerance:
        val_str = str(int(round(val)))
    else:
        val_str = ('%.6f' % val).rstrip('0').rstrip('.')
    print(f"x{i + 1} = {val_str}")