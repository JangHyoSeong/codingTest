A, B = map(int, input().split())

a_str = sorted(str(A), reverse=True)
used = [False] * len(a_str)
best = -1

def make_permutation(path):
    global best

    if len(path) == len(a_str):
        num = int("".join(path))
        if num < B:
            best = max(best, num)
        return
    
    for i in range(len(a_str)):
        if used[i]:
            continue

        if i > 0 and a_str[i] == a_str[i-1] and not used[i-1]:
            continue

        if len(path) == 0 and a_str[i] == "0":
            continue

        used[i] = True
        make_permutation(path + [a_str[i]])
        used[i] = False

make_permutation([])
print(best)