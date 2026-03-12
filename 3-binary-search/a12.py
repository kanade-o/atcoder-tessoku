N, K = map(int, input().split())
A = list(map(int, input().split()))


def check(X: int, N: int, K: int, A: list) -> bool:
    sum = 0
    for i in range(N):
        sum += X // A[i]

    if sum >= K:
        return True
    return False


L = 0
R = 10**9
while (
    L < R
):  # このタイプの二分探索は L < Rとする. LとRが答えとなるので, L == Rではそのままにしておきたい
    mid = (L + R) // 2
    ans = check(mid, N, K, A)
    if not ans:  # Kよりもmidまでの合計が小さかった場合, Lをmid + 1にする
        L = mid + 1
    else:  # Kよりもmidまでの合計が大きかった場合 or K = sum(mid)の場合, Rをmidに合わせる.
        R = mid
print(L)
