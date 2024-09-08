from collections import deque

N, K = map(int, input().split())
number = [int(digit) for digit in str(N)]
number_len = len(number)

q = deque()
result = set()
used = [set() for _ in range(K+1)]

q.append([number, 0])

while q:
    now_number, count = q.popleft()

    if count == K:
        result.add(int(''.join(map(str, now_number))))
        

    if count < K:
        for i in range(number_len):
            for j in range(i+1, number_len):

                now_number[i], now_number[j] = now_number[j], now_number[i]
                int_number = int(''.join(map(str, now_number)))

                if now_number[0] != 0 and not int_number in used[count+1]:
                    q.append([now_number[:], count+1])
                    used[count+1].add(int_number)

                now_number[i], now_number[j] = now_number[j], now_number[i]

if result:
    print(max(result))
else:
    print(-1)