T = int(input())

def validate_graph(n, m, edges):

    nodes = [0] * (n+1)
    for i in range(1, n+1):

        if nodes[i]:
            continue

        stack = [i]
        nodes[i] = 1

        while stack:
            now = stack.pop()
            now_color = nodes[now]

            for next in edges[now]:
                if nodes[now] == nodes[next]:
                    return 'impossible'
                    
                
                elif nodes[next] == 0:
                    stack.append(next)
                    nodes[next] = 3 - nodes[now]

    return 'possible'
    

for testcase in range(T):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())

        edges[a].append(b)
        edges[b].append(a)

    print(validate_graph(n, m, edges))