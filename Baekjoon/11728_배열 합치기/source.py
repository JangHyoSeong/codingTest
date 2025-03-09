import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A_idx, B_idx = 0, 0

new_arr = [None] * (N + M)
for i in range(N + M):

    if A_idx >= N:
        new_arr[i] = B[B_idx]
        B_idx += 1
    
    elif B_idx >= M:
        new_arr[i] = A[A_idx]
        A_idx += 1

    else:
        if A[A_idx] < B[B_idx]:
            new_arr[i] = A[A_idx]
            A_idx += 1
        else:
            new_arr[i] = B[B_idx]
            B_idx += 1

print(" ".join(map(str, new_arr)))