N = int(input())
arr = list(map(int, input().split()))

now_num = 1
stack = []
for num in arr:
    if num == now_num:
        now_num += 1
        
        while stack:
            if stack[-1] == now_num:
                stack.pop()
                now_num += 1
            
            else:
                break
    
    else:
        stack.append(num)

print("Sad" if stack else "Nice")