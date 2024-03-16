def permutation(i, M, N, arr):
    arr = arr[:]

    if M == 0:
        for num in arr:
            print(num, end= ' ')
        print()
        return
    
    for j in range(i+1, N+1):
        if N-j < M-1:
            return
        permutation(j, M-1, N, arr + [j])
        

N, M = map(int, input().split())

permutation(0, M, N, [])