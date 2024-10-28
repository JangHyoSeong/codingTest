from collections import deque

s = input()

count = 0
a_q = deque()
b_q = deque()
c_q = deque()

for i in range(len(s)-1, -1, -1):
    if s[i] == 'A':
        a_q.append(i)
    elif s[i] == 'B':
        b_q.append(i)
    else:
        c_q.append(i)

while a_q:
    a_idx = a_q.popleft()
    if b_q:
        if a_idx < b_q[0]:
            count += 1
            b_q.popleft()
    else:
        break

while b_q:
    b_idx = b_q.popleft()
    if c_q:
        if b_idx < c_q[0]:
            count += 1
            c_q.popleft()

print(count)