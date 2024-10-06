import sys
from heapq import heappop, heappush
from collections import deque

N, M, K = map(int, input().split())

# 각 줄을 나타내는 큐 생성
lines = [deque() for _ in range(M)]
for i in range(N):
    d, h = map(int, sys.stdin.readline().rstrip().split())
    lines[i % M].append((d, h, i))

# 힙 초기화
heap = []
for i in range(M):
    if lines[i]:
        d, h, idx = lines[i].popleft()
        heappush(heap, (-d, -h, i, idx))  # (근무일수, 화장실 급함 정도, 줄 번호, 원래 인덱스)

count = 0
while heap:
    d, h, line_idx, idx = heappop(heap)

    # 데카의 차례인지 확인
    if idx == K:
        break

    # 현재 줄에서 다음 사람을 힙에 추가
    if lines[line_idx]:
        d, h, idx = lines[line_idx].popleft()
        heappush(heap, (-d, -h, line_idx, idx))
    
    count += 1

print(count)
