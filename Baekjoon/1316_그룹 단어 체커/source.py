N = int(input())

count = 0
for _ in range(N):
    string = input()
    char_set = set()

    for i in range(len(string)):
        if string[i] in char_set:
            if string[i] != string[i-1]:
                break
        else:
            char_set.add(string[i])
    
    else:
        count += 1

print(count)