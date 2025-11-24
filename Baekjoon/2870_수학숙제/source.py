N = int(input())

numbers = []
for _ in range(N):
    line = input()
    temp = ""
    for c in line:
        if c.isdigit():
            temp += c
        else:
            if temp != "":
                numbers.append(int(temp))
                temp = ""
    
    if temp != "":
        numbers.append(int(temp))

numbers.sort()

for n in numbers:
    print(n)