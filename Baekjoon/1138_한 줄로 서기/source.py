N = int(input())
arr = list(map(int, input().split()))

line = [0] * N

for i in range(N):
    count = arr[i]
    for j in range(N):
        if count == 0 and line[j] == 0:
            line[j] = i+1
            break

        elif line[j] == 0:
            count -= 1

print(" ".join(map(str, line)))