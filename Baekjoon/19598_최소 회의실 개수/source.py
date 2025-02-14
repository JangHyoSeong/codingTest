from heapq import heappop, heappush

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort()

pq = []
room = 0
max_room = 0
for meeting in meetings:
    heappush(pq, meeting[1])
    room += 1
    
    while pq:
        now_meeting = heappop(pq)

        if meeting[0] >= now_meeting:
            room -= 1
        else:
            heappush(pq, now_meeting)
            break
    
    max_room = max(max_room, room)

print(max_room)