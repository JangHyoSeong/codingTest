import sys

string = sys.stdin.readline().rstrip()
n = len(string)

all_same = True
for i in range(1, n):
    if string[i] != string[0]:
        all_same = False
        break

if all_same:
    print(-1)
    sys.exit()

left, right = 0, n-1
is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(n-1 if is_palindrome else n)