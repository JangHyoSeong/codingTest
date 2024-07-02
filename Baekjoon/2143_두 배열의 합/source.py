from collections import Counter

def find_subarray_sums(arr):
    subarray_sums = []
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            subarray_sums.append(current_sum)
    return subarray_sums

def count_pairs_with_sum(A, B, T):
    subarray_sums_A = find_subarray_sums(A)
    subarray_sums_B = find_subarray_sums(B)
    
    # Counter를 통해 각 합의 등장 횟수를 셈
    count_B = Counter(subarray_sums_B)
    
    count = 0
    for sum_A in subarray_sums_A:
        required_B = T - sum_A
        if required_B in count_B:
            count += count_B[required_B]
    
    return count

# 입력
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 결과 출력
result = count_pairs_with_sum(A, B, T)
print(result)