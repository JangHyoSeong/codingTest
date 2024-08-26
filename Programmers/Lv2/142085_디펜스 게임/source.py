from heapq import heappush, heappop

def solution(n, k, enemy):
    pq = []
    total = 0
    
    round_len = len(enemy)
    for i in range(round_len):
        heappush(pq, -enemy[i])
        total += enemy[i]
        
        if total > n:
            if k > 0:
                total += heappop(pq)
                k -= 1
            else:
                return i
    
    return round_len