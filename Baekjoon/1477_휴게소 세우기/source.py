N, M, L = map(int, input().split())

if N != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

arr.append(0)
arr.append(L)
arr.sort()

sections = []
for i in range(1, len(arr)):
    sections.append(arr[i] - arr[i-1])

def can_build(max_dist):
    count = 0
    for section in sections:
        if section > max_dist:
            count += (section - 1) // max_dist
    
    return count <= M

left, right = 1, L
answer = 0

while left <= right:
    mid = (left + right) // 2
    if can_build(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)