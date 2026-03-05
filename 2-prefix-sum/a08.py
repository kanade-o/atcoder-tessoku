H, W = map(int, input().split())
X = [[int(x) for x in input().split()] for _ in range(H)]
Q = int(input())
A, B, C, D = [0] * Q, [0] * Q, [0] * Q, [0] * Q
for j in range(Q):
    A[j], B[j], C[j], D[j] = map(int, input().split())

Z = [[0] * (W + 1) for _ in range(H + 1)]
# 横の累積和
for h_i in range(H):
    for w_i in range(W):
        Z[h_i + 1][w_i + 1] = (
            Z[h_i + 1][w_i] + X[h_i][w_i]
        )  # Z[0][0:W]とZ[0:H][0]は0にしておく

# 縦の累積和
for w_i in range(W + 1):  # インデックスを+1しないといけない
    for h_i in range(H):
        Z[h_i + 1][w_i] = (
            Z[h_i][w_i] + Z[h_i + 1][w_i]
        )  # 横の累積和の結果を使うことに注意

for q_i in range(Q):
    ans = (
        Z[C[q_i]][D[q_i]]
        - Z[A[q_i] - 1][D[q_i]]
        - Z[C[q_i]][B[q_i] - 1]
        + Z[A[q_i] - 1][B[q_i] - 1]
    )
    print(ans)
