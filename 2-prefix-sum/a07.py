D = int(input())
N = int(input())
L, R = [0] * N, [0] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

diff = [0] * (D + 1)
for p_i in range(N):
    day_in, day_out = L[p_i] - 1, R[p_i] - 1  # インデックスを揃える
    diff[day_in] += 1
    diff[day_out + 1] -= 1

S = [0] * (D + 1)
for i in range(D):  # 累積和の計算
    S[i + 1] = S[i] + diff[i]

for i in range(1, D + 1):
    print(S[i])
