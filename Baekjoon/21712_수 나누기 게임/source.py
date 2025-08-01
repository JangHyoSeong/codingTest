import sys

MAX = 1000000

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

score = [0] * N
value_to_index = {x: i for i, x in enumerate(arr)}

for i in range(N):
    x = arr[i]
    mul = x * 2

    while mul <= MAX:
        if mul in value_to_index:
            j = value_to_index[mul]
            score[i] += 1
            score[j] -= 1
        mul += x

print(" ".join(map(str, score)))