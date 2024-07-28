import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        print(f"Step {k+1}:\n{np.array(M)}\n")
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = float(M[n-1][n]) / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z += float(M[i][j]) * x[j]
        x[i] = float(M[i][n] - z) / M[i][i]
    print(f"Solution:\n{x}\n")
    return x

# matrix goes here
A = np.array([[2, 1, -1],[-3, -1, 2],[-2, 1, 2]], dtype='float')
# solution vector goes here
b = np.array([8, -11, -3], dtype='float')

gaussian_elimination(A.tolist(), b.tolist())
# idk, its supposed to show its steps, but honestly who cares.
