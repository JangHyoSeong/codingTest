N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = -int(1e9)
min_result = int(1e9)

def calc(idx, result, plus, minus, multiply, divide):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    num = arr[idx]
    
    if plus > 0:
        calc(idx + 1, result + num, plus - 1, minus, multiply, divide)
    if minus > 0:
        calc(idx + 1, result - num, plus, minus - 1, multiply, divide)
    if multiply > 0:
        calc(idx + 1, result * num, plus, minus, multiply - 1, divide)
    if divide > 0:
        
        if result < 0:
            calc(idx + 1, -(-result // num), plus, minus, multiply, divide - 1)
        else:
            calc(idx + 1, result // num, plus, minus, multiply, divide - 1)

calc(1, arr[0], *operators)

print(max_result)
print(min_result)