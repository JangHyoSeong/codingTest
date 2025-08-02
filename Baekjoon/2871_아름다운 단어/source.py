import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()

used = [False] * N
pq = []

for i in range(N):
    heappush(pq, (word[i], -i))

sang = []
hee = []

right = N-1
for turn in range(N):
    if turn % 2 == 0:
        while used[right]:
            right -= 1
        
        sang.append(word[right])
        used[right] = True
    
    else:
        while pq:
            char, idx = heappop(pq)
            if not used[-idx]:
                hee.append(char)
                used[-idx] = True
                break

            
hee_word = "".join(map(str, hee))
sang_word = "".join(map(str, sang))

print("DA" if hee_word < sang_word else "NE")
print(hee_word)