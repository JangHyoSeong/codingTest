import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
lights = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = lights[0], N
answer = N

while left <= right:
    mid = (left + right) // 2

    flag = True

    if lights[0] - mid > 0:
        flag = False

    for i in range(1, M):
        if lights[i] - lights[i-1] > 2 * mid:
            flag = False
            break
    
    if lights[-1] + mid < N:
        flag = False

    if flag:
        answer = mid
        right = mid - 1
    
    else:
        left = mid + 1

print(answer)