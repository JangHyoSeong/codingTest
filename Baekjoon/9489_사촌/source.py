import sys
from collections import deque

while True:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and k == 0:
        break

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    parent = {arr[0]: -1}
    nodes = deque()
    nodes.append(arr[0])

    idx = 1

    while idx < n:
        start_idx = idx

        while idx + 1 < n and arr[idx + 1] == arr[idx] + 1:
            idx += 1
        
        end_idx = idx

        parent_node = nodes.popleft()
        for i in range(start_idx, end_idx + 1):
            parent[arr[i]] = parent_node
            nodes.append((arr[i]))
        
        idx += 1
    
    if k not in parent:
        print(0)
        continue

    p = parent[k]
    if p == -1 or parent[p] == -1:
        print(0)
        continue

    grand = parent[p]
    cousins = 0
    for node, par in parent.items():
        if par != p and par != -1 and parent.get(par, -1) == grand:
            cousins += 1
    
    print(cousins)