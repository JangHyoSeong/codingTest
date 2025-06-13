import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

count = 0
i = 0
pattern = 0

while i < M - 1:
    if S[i] == "I" and S[i+1] == "O":
        j  = i + 1
        while j + 1 < M and S[j] == "O" and S[j+1] == "I":
            pattern += 1
            j += 2
            if pattern == N:
                count += 1
                pattern -= 1
        i = j
        pattern = 0
    
    else:
        i += 1

print(count)