N = int(input())
words = [list(input()) for _ in range(N)]

for word in words:
    i = len(word) - 1

    while i > 0 and word[i-1] >= word[i]:
        i -= 1
    
    if i == 0:
        print("".join(map(str, word)))
        continue

    j = len(word) - 1
    while word[i-1] >= word[j]:
        j -= 1

    word[i-1], word[j] = word[j], word[i-1]
    word[i:] = sorted(word[i:])
    
    print("".join(map(str, word)))