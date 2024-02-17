N = int(input())
switch = list(map(int, input().split()))
M = int(input())

arr = [list(map(int, input().split())) for _ in range(M)]


for i in range(M):
    if arr[i][0] == 1:
        for j in range(arr[i][1]-1, N, arr[i][1]):
            switch[j] = (switch[j]+1)%2
    else:
        idx = 0
        center = arr[i][1]-1
        while center - idx >= 0 and center + idx < N:
            if idx == 0:
                switch[center] = (switch[center]+1)%2
            elif switch[center + idx] == switch[center - idx]:
                switch[center + idx] = (switch[center + idx]+1)%2
                switch[center - idx] = (switch[center - idx]+1)%2
                
            else:
                break
            idx += 1
            


for i in range(0, N):
    print(switch[i], end=' ')
    if i%20 == 19:
        print()