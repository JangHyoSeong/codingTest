def get_length(k):
    if k == 0:
        return 3
    
    if length[k] != -1:
        return length[k]
    
    length[k] = get_length(k-1) * 2 + (k+3)

    return length[k]

def solve(n, k):
    if k == 0:
        return "moo"[n-1]
    
    left = get_length(k-1)
    middle = k + 3

    if n <= left:
        return solve(n, k-1)
    
    elif n <= left + middle:
        if n - left == 1:
            return "m"
        
        else:
            return "o"
    
    else:
        return solve(n - left - middle, k - 1)

N = int(input())

length = [-1] * 32
k = 0

while get_length(k) < N:
    k += 1

print(solve(N, k))