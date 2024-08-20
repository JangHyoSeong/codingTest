N = int(input())
arr = list(map(int, input().split()))

num_map = {num: True for num in arr}

# 수열의 시작점을 찾는다.
for num in arr:
    found = True
    current = num
    for _ in range(N - 1):
        if current % 3 == 0 and num_map.get(current // 3, False):
            current //= 3
        elif num_map.get(current * 2, False):
            current *= 2
        else:
            found = False
            break
    if found:
        start_num = num
        break

# 수열 A를 구성한다.
result = [start_num]
for _ in range(N - 1):
    current = result[-1]
    if current % 3 == 0 and num_map.get(current // 3, False):
        result.append(current // 3)
    elif num_map.get(current * 2, False):
        result.append(current * 2)

print(" ".join(map(str, result)))
