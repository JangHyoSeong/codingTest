from copy import deepcopy

def solution(info, edges):
    N = len(info)
    graph = [[] for _ in range(N)]
    
    for edge in edges:
        graph[edge[0]].append(edge[1])

    max_sheep = 0
    
    def dfs(sheep, wolf, available):
        nonlocal max_sheep
        max_sheep = max(max_sheep, sheep)
        
        for idx, node in enumerate(available):
            next_available = deepcopy(available)
            next_available.pop(idx)
            next_available.extend(graph[node])
            
            if info[node] == 0:
                dfs(sheep + 1, wolf, next_available)
            else:
                if sheep > wolf + 1:
                    dfs(sheep, wolf + 1, next_available)
    
    dfs(1, 0, graph[0])
        
        
    return max_sheep