N = int(input())
A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N
for q in range(N):
    A[q], B[q], C[q], D[q] = map(int, input().split())

masu = [[0] * (1500 + 1) for _ in range(1500 + 1)]
for q in range(N):  # マスではなく座標なので, 長方形のとる範囲に注意. +1とかしなくて良い
    masu[A[q]][B[q]] += 1
    masu[C[q]][D[q]] += 1
    masu[C[q]][B[q]] -= 1
    masu[A[q]][D[q]] -= 1

for x in range(0, 1500 + 1):
    for y in range(1, 1500 + 1):
        masu[x][y] = masu[x][y - 1] + masu[x][y]

for y in range(0, 1500 + 1):
    for x in range(1, 1500 + 1):
        masu[x][y] = masu[x - 1][y] + masu[x][y]


ans = 0
for y in range(1500 + 1):
    for x in range(1500 + 1):
        if not masu[y][x] == 0:
            ans += 1
print(ans)
