N, K = map(int, input().split())
arr = list(map(int, input().split()))

global count
count = 0

global result
result = -1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result
    tmp = []
    i, j = p, q + 1

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    for t in range(len(tmp)):
        A[p + t] = tmp[t]
        count += 1
        if count == K:
            result = tmp[t]

merge_sort(arr, 0, N - 1)
print(result)