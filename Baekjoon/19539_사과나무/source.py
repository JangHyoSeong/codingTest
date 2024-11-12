N = int(input())
trees = list(map(int, input().split()))

height_sum = sum(trees)
if height_sum % 3:
    print('NO')
    exit()

two_count = 0
for tree in trees:
    two_count += tree // 2

if two_count >= height_sum // 3:
    print('YES')
else:
    print('NO')
