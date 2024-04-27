from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 오름차순 정렬된 리스트를 만들고 정답과 비교함
sorted_arr = sorted(arr)

# 이미 만든 arr는 만들지 않기 위해 딕셔너리를 통해 방문 여부를 검사
already_make = {}
# BFS를 위해 queue를 선언
# 현재 arr와, count를 담고 있음
q = deque([[arr, 0]])


# BFS 시작
while q:
    # 현재 arr, count
    now, count = q.popleft()

    # 오름차순 정렬되었다면 count를 출력하고 종료
    if now == sorted_arr:
        print(count)
        break

    # 아니라면 BFS, 모든 경우를 전부 검사함
    for i in range(N-K+1):
        # K개 만큼 뒤집기 위해서 사용
        temp_arr = now[i:i+K]

        # K개 만큼 뒤집은 새로운 arr
        new = now[:i] + temp_arr[::-1] + now[i+K:]

        # 딕셔너리의 key값으로 쓰기 위해 튜플(불변)으로 만듦
        tuple_new = tuple(new)

        # 만약 딕셔너리에 존재하지 않는다면

        if already_make.get(tuple_new) is None:
            # q에 삽입, 방문처리를 해줌
            q.append([new, count+1])
            already_make[tuple_new] = True
# break되지 않고 끝났다면 -1 출력
else:
    print(-1)