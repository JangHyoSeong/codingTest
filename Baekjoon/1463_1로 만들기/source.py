n = int(input())

count = [0, 0, 1, 1]

for i in range(4, n+1):
    val1 = 1 + count[i-1]
    val2 = 1 + count[i-1]
    val3 = 1+ count[i-1]

    if i%3 == 0:
        val2 = 1 + count[i//3]
    if i%2 == 0:
        val3 = 1 + count[i//2]

    count.append(min(val1, val2, val3))
    
print(count[n])