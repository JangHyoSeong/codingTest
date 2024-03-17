def AtoB(a, b, cnt):
    global min_cnt
    if a == b:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    elif a>b:
        return

    AtoB(a*10 + 1, b, cnt+1)
    AtoB(a*2, b, cnt+1)
        

A, B = map(int, input().split())
min_cnt = 2**31 - 1

AtoB(A, B, 1)

if min_cnt == 2**31-1:
    print(-1)
else:
    print(min_cnt)