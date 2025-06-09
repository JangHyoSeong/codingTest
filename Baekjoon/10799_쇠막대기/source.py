import sys

arr = sys.stdin.readline().rstrip()
arr_len = len(arr)

count = 0
steel = 0

for i in range(arr_len - 1):
    if arr[i] == "(" and arr[i+1] == "(":
        count += 1
        steel += 1

    elif arr[i] == "(" and arr[i+1] == ")":
        steel += count
    
    elif arr[i] == ")" and arr[i+1] == ")":
        count -= 1

print(steel)