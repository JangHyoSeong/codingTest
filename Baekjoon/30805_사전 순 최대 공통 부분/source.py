n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

flag = True
ans = []

while True:
    # Find the maximum common value in both sequences
    while True:
        if len(a) == 0 or len(b) == 0:
            flag = False
            break
        max_a = max(a)
        a_idx = a.index(max_a)
        max_b = max(b)
        b_idx = b.index(max_b)
        if max_a == max_b:
            break
        elif max_a > max_b:
            a.pop(a_idx)
        else:
            b.pop(b_idx)
    
    if not flag:
        break
    
    # Push the maximum value to ans
    ans.append(max_a)
    
    # Remove elements smaller than the maximum value
    a = a[a_idx+1:]
    b = b[b_idx+1:]

if ans:
    print(len(ans))
    print(" ".join(map(str, ans)))
else:
    print(0)