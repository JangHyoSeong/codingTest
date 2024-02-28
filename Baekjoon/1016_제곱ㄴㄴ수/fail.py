from math import sqrt

a, b = map(int, input().split())

arr = [2]

i = 3
while i < sqrt(b):
    for num in arr:
        if i % num == 0:
            break
    else:
        arr.append(i)
    
    i+= 1

valid = [True] * (b-a+1)

for i in range(a, b+1):
    if valid[i-a] == False:
        continue
    for num in arr:
        if i < num ** 2:
            break
        if i % num**2 == 0:
            valid[i-a] = False

print(valid.count(True))