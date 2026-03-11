N, X = map(int, input().split())
A = list(map(int, input().split()))

low, high = 0, N - 1
while low <= high:
    mid = (low + high) // 2
    if A[mid] < X:
        low = mid + 1
    elif A[mid] > X:
        high = mid - 1
    else:
        print(mid + 1)
        break
