string = list(input())
a_count = string.count('a')
n = len(string)

if a_count == 0 or a_count == n:
    print(0)
    exit()

extended = string * 2

b_count = extended[:a_count].count('b')
min_swaps = b_count

for i in range(a_count, len(extended)):
    if extended[i] == 'b':
        b_count += 1
    
    if extended[i - a_count] == 'b':
        b_count -= 1
    
    min_swaps = min(min_swaps, b_count)

print(min_swaps)