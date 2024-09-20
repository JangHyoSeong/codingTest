def is_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

T = int(input())
arr = [input() for _ in range(T)]

for string in arr:
    
    start, end = 0, len(string)-1
    result = 0

    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            if is_palindrome(string, start+1, end) or is_palindrome(string, start, end-1):
                result = 1
            else:
                result = 2
            break
        
    print(result)