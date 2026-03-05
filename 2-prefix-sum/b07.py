T = int(input())
N = int(input())
L, R = [0] * N, [0] * N
for j in range(N):
    L[j], R[j] = map(int, input().split())

diff = [0] * (T + 1)
for j in range(N):
    diff[L[j]] += 1
    diff[R[j]] -= 1
print(diff)

S = [0] * (T + 1)
for i in range(T):
    S[i + 1] = S[i] + diff[i]
print(S)

for i in range(1, T + 1):
    print(S[i])
