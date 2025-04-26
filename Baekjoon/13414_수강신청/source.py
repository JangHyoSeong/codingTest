import sys

K, L = map(int, sys.stdin.readline().rstrip().split())
wait_list = {}

for _ in range(L):
    student_id = sys.stdin.readline().rstrip()

    if student_id in wait_list:
        del wait_list[student_id]

    wait_list[student_id] = True

for i, student_id in enumerate(wait_list):
    if i >= K:
        break
    print(student_id)