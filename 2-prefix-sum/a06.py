N, Q = map(int, input().split())
A = list(map(int, input().split()))
L, R = [0] * Q, [0] * Q
for q_i in range(Q):
    L[q_i], R[q_i] = map(int, input().split())

S = [0] * (N + 1)  # S[0] = 0
for s_i in range(N):
    S[s_i + 1] = S[s_i] + A[s_i]

for q_i in range(Q):
    print(S[R[q_i]] - S[L[q_i] - 1])
