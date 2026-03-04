N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L, R = [0] * Q, [0] * Q
for q_i in range(Q):
    L[q_i], R[q_i] = map(int, input().split())

atari = [0] * (N + 1)
hazure = [0] * (N + 1)
for i in range(N):
    if A[i] == 1:
        atari[i + 1] = atari[i] + 1
        hazure[i + 1] = hazure[i]
    else:  # A[i] == 0
        atari[i + 1] = atari[i]
        hazure[i + 1] = hazure[i] + 1

for q_i in range(Q):
    num_atari = atari[R[q_i]] - atari[L[q_i] - 1]
    num_hazure = hazure[R[q_i]] - hazure[L[q_i] - 1]
    if num_hazure < num_atari:
        print("win")
    elif num_hazure > num_atari:
        print("lose")
    else:
        print("draw")
