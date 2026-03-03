N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * Q
R = [0] * Q
for j in range(Q):
    L[j], R[j] = map(int, input().split())

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])
