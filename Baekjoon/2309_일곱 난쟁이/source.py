arr = []
for i in range(9):
    arr.append(int(input()))

man_sum = sum(arr)
flag = False
for i in range(9):
    for j in range(i+1, 9):
        if man_sum - arr[i] - arr[j] == 100:
            arr.pop(i)
            arr.pop(j-1)
            flag = True
        if flag == True:
            break
    if flag == True:
        break
arr.sort()
for i in arr:
    print(i)