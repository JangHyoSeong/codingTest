hour, minute = map(int, input().split())

if minute - 45 < 0:
    minute += 15
    if hour == 0:
        hour = 23
    else:
        hour -=1
else:
    minute -= 45

print(hour, minute)

'''
숏코딩
a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)
'''