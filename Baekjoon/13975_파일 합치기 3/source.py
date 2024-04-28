from heapq import heappush, heappop

# 테스트케이스 개수 입력받음
T = int(input())

for testcase in range(T):
    # 입력받음
    N = int(input())
    files = list(map(int, input().split()))

    # 파일 합치는 비용
    cost = 0

    '''
    파이썬은 내장 모듈로 heap이 존재한다
    heappush, heappop을 통해 우선순위 큐를 구현할 수 있다

    이 문제에서 우선순위 큐를 사용해야 하는 이유
    파일을 합칠 때 작은 파일부터 순서대로 합치는 것이 최소값을 구하는 방법이다
    그렇기에 파일을 합친 후에 새로 생성된 파일의 크기 또한, 원래 파일과 비교해서
    우선순위 큐에 넣어야한다. 이를 위해 힙을 사용한다
    '''

    # 우선순위 큐로 사용할 pq. (힙)
    pq = []
    
    # 힙에 모든 파일들을 삽입한다
    for i in range(N):
        heappush(pq, files[i])

    # 파일의 개수. 모든 파일이 합쳐질 때까지 반복
    i = N-1
    while i > 0:

        # 파일 두개를 힙에서 빼낸다 (가장 작은 수 2개)
        a, b = heappop(pq), heappop(pq)

        # 새로운 파일을 만들고 heap에 push한다
        new_file = a+b
        heappush(pq, new_file)

        # 파일 합치는 비용을 더해주고, 파일 2개가 1개가 됐으므로 인덱스를 1 감소시킨다
        cost += new_file
        i -= 1

    print(cost)