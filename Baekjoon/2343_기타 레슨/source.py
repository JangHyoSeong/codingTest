def minimum_bluray_size(n, m, lessons):
    def can_divide(size):
        count = 1
        total = 0
        for lesson in lessons:
            if total + lesson > size:
                count += 1
                total = lesson
                if count > m:
                    return False
            else:
                total += lesson
        return True
    
    left = max(lessons)
    right = sum(lessons)
    
    while left < right:
        mid = (left + right) // 2
        if can_divide(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

print(minimum_bluray_size(n, m, lessons))