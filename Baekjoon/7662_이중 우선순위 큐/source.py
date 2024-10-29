import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    
    min_heap = []
    max_heap = []
    visited = [False] * (k + 1)  # 삭제 여부를 추적하기 위한 배열

    for i in range(k):
        operation, num = input().split()
        num = int(num)
        
        if operation == 'I':
            # 삽입 연산
            heapq.heappush(min_heap, (num, i))  # 최소 힙에 삽입
            heapq.heappush(max_heap, (-num, i))  # 최대 힙에 삽입
            visited[i] = True  # 해당 인덱스는 아직 삭제되지 않음
            
        elif operation == 'D':
            if num == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)  # 이미 삭제된 값은 무시
                if max_heap:
                    visited[max_heap[0][1]] = False  # 실제로 삭제
                    heapq.heappop(max_heap)
            elif num == -1:  # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)  # 이미 삭제된 값은 무시
                if min_heap:
                    visited[min_heap[0][1]] = False  # 실제로 삭제
                    heapq.heappop(min_heap)
    
    # 최종적으로 유효한 값만 남기기 위해서
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
