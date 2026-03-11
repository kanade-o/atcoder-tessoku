N = int(input())
A = list(map(int, input().split()))
D = int(input())
L, R = [0] * D, [0] * D
for d_i in range(D):
    L[d_i], R[d_i] = map(int, input().split())

P, Q = [0] * N, [0] * N
# 先頭からの累積max
P[0] = A[0]
for i in range(1, N):
    P[i] = max(P[i - 1], A[i])

# 末尾からの累積max
Q[N - 1] = A[N - 1]
for i in reversed(range(0, N - 1)):
    Q[i] = max(Q[i + 1], A[i])

# クエリに答える
for d_i in range(D):
    ans = max(P[(L[d_i] - 1) - 1], Q[(R[d_i] + 1) - 1])
    print(ans)
