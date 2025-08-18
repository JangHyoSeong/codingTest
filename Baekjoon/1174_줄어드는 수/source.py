from itertools import combinations

N = int(input())

nums = []

for length in range(1, 11):
    for comb in combinations(range(10), length):
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        nums.append(num)

nums.sort()

if N > len(nums):
    print(-1)

else:
    print(nums[N-1])