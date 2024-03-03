N = int(input())
arr = list(map(int, input().split()))
students = []
stack = []

for i in range(N):
    if arr[i] == 0:
        students.append(i+1)
    else:
        for j in range(arr[i]):
            stack.append(students.pop())
        students.append(i+1)
        for j in range(arr[i]):
            students.append(stack.pop())

print(" ".join(map(str, students)))