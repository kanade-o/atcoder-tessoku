H, W, N = map(int, input().split())
A, B, C, D = (
    [0] * N,
    [0] * N,
    [0] * N,
    [0] * N,
)
for q in range(N):
    A[q], B[q], C[q], D[q] = map(int, input().split())

masu = [[0] * (W + 2) for _ in range(H + 2)]  # +2してindex errorにならないようにする.
# 差分を求める
for q in range(N):
    masu[A[q]][B[q]] += 1
    masu[C[q] + 1][D[q] + 1] += 1
    masu[A[q]][D[q] + 1] -= 1
    masu[C[q] + 1][B[q]] -= 1

# 横の累積和
for h_i in range(1, H + 1):
    for w_i in range(1, W + 1):
        masu[h_i][w_i] = masu[h_i][w_i - 1] + masu[h_i][w_i]

# 縦の累積和
for w_i in range(1, W + 1):
    for h_i in range(1, H + 1):
        masu[h_i][w_i] = masu[h_i - 1][w_i] + masu[h_i][w_i]

for h_i in range(1, H + 1):
    for w_i in range(1, W + 1):
        print(masu[h_i][w_i], end=" ")
    print("")
