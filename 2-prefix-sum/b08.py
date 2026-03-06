N = int(input())
X, Y = [0] * N, [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())
A, B, C, D = [0] * Q, [0] * Q, [0] * Q, [0] * Q
for j in range(Q):
    A[j], B[j], C[j], D[j] = map(int, input().split())

# 点の情報を二次元配列に反映
matrix_size = 1500 + 1
Z = [[0] * matrix_size for _ in range(matrix_size)]
for i in range(N):
    Z[Y[i]][X[i]] += 1

S = [[0] * matrix_size for _ in range(matrix_size)]
# 横の累積和
for y_i in range(1, matrix_size):
    for x_i in range(1, matrix_size):
        S[y_i][x_i] = S[y_i][x_i - 1] + Z[y_i][x_i]
# 縦の累積和
for x_i in range(1, matrix_size):
    for y_i in range(1, matrix_size):
        S[y_i][x_i] = S[y_i - 1][x_i] + S[y_i][x_i]


for i in range(Q):
    ans = S[D[i]][C[i]] - S[B[i] - 1][C[i]] - S[D[i]][A[i] - 1] + S[B[i] - 1][A[i] - 1]
    print(ans)
