N = int(input())

def func(n):
    digits = list(map(int, str(n)))
    if len(digits) <= 2:
        return True
    
    return digits[0] - digits[1] == digits[1] - digits[2]

count = 0
for i in range(1, N+1):
    if func(i):
        count += 1

print(count)