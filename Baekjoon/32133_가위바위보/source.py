from collections import deque

def solve():
    N, M, K = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    # BFS로 각 상태를 탐색
    queue = deque([(0, list(range(N)), [])])
    
    while queue:
        round, remaining, moves = queue.popleft()
        
        if len(remaining) == 0:
            continue

        if len(remaining) <= K:
            print(round)
            print("".join(moves))
            return
        
        if round == M:
            continue

        
        # 가능한 피돌이의 선택을 모두 시도 (R, S, P)
        if round < M:
            for move in ['R', 'S', 'P']:
                new_remaining = []
                for i in remaining:
                    # 피돌이가 무엇을 내야 친구 i가 탈락하는지 계산
                    if (move == 'R' and arr[i][round] == 'P') or \
                    (move == 'S' and arr[i][round] == 'R') or \
                    (move == 'P' and arr[i][round] == 'S'):
                        new_remaining.append(i)
                        
                
                queue.append((round + 1, new_remaining, moves + [move]))
    
    # 가능한 모든 경우를 시도했지만 방법이 없는 경우
    print(-1)

solve()