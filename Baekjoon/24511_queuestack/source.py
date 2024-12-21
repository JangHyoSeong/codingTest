from collections import deque

N = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
M = int(input())
input_numbers = list(map(int, input().split()))

new_arr = deque()
for i in range(N):
    if arr_1[i] == 0:
        new_arr.append(arr_2[i])


for number in input_numbers:
    new_arr.appendleft(number)
    print(new_arr.pop(), end=" ")