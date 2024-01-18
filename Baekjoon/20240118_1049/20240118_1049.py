n, m = map(int,input().split())

minPackage = 1000
minOne = 1000
answer = 0


for i in range(m):
    a, b = map(int,input().split())

    if a < minPackage:
        minPackage = a
    if b < minOne:
        minOne = b

min_cost = min(minPackage * (n//6) + minOne * (n%6), minPackage * ((n + 5)//6))

print(min_cost)