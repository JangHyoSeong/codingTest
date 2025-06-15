import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_max = [0] * N
prefix_max[N-1] = arr[N-1]

for i in range(N-2, -1, -1):
    prefix_max[i] = max(prefix_max[i+1], arr[i])

left_max, right_max = 0, prefix_max[0]
left_win, right_win = 0, 0

for i in range(N-1):
    left_max = max(left_max, arr[i])
    right_max = prefix_max[i+1]    

    if left_max > right_max:
        left_win += 1
    
    elif left_max < right_max:
        right_win += 1


if left_win > right_win:
    print("R")

elif left_win < right_win:
    print("B")

else:
    print("X")