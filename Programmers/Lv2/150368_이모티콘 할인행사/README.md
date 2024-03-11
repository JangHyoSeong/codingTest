# 이모티콘 할인행사

## **📝문제 설명**
문제 링크 참조

## **🧐CODE REVIEW**

### **😫나의 오답 풀이**

### **🧾나의 풀이**

```python
sale_percent = [10, 20, 30, 40]

def find_max(i, emoji_num, sales, emoji_price, users, users_num):
    global max_plus
    global max_price
    new_sales = sales[:]

    if i == emoji_num:
        now_plus = 0
        now_price = 0
        for k in range(users_num):
            user_price = 0

            for j in range(emoji_num):
                if users[k][0] <= new_sales[j]:
                    user_price += emoji_price[j] * (100 - new_sales[j]) / 100
                    if user_price >=  users[k][1]:
                        now_plus += 1
                        break
            else:
                now_price += user_price

            if users_num - (k+1) + now_plus < max_plus:
                return
            
        if max_plus < now_plus:
            max_plus = now_plus
            max_price = now_price

        elif max_plus == now_plus:
            if max_price < now_price:
                max_price = now_price


    else:
        for j in range(4):
            new_sales[i] = sale_percent[j]
            find_max(i+1, emoji_num, new_sales, emoji_price, users, users_num)


def solution(users, emoticons):
    global max_plus
    global max_price
    max_plus = 0
    max_price = 0
    answer = []

    emoji_num = len(emoticons)
    user_num = len(users)
    sales_arr = [10] * emoji_num

    find_max(0, emoji_num, sales_arr, emoticons, users, user_num)
    
    answer = [max_plus, max_price]

    return answer
```

#### **📝해설**

```python
# 할인율 테이블
sale_percent = [10, 20, 30, 40]

def find_max(i, emoji_num, sales, emoji_price, users, users_num):
    # 재귀적으로 호출되며 정답을 찾는 함수
    '''
    i : 이모티콘의 할인율을 섞어줄 인덱스, i번째 이모티콘의 할인율을 결정
    emoji_num, emoji_price : 이모티콘의 개수, 가격
    sales : 현재 이모티콘들의 할인율을 담고 있는 리스트
    users, users_num : 유저 리스트, 유저 리스트의 길이
    '''
    
    # 결과로 사용될 max_plus, max_price를 전역 변수로 선언
    global max_plus
    global max_price

    # 얕은 복사를 피하기 위해 새롭게 설정할 할인율 리스트를 슬라이싱을 통해 가져옴
    new_sales = sales[:]

    # 모든 이모티콘의 할인율을 설정했다면
    if i == emoji_num:

        # 이 함수에서의 plus가입자수, 최대 가격을 0으로 시작
        now_plus = 0
        now_price = 0

        # 모든 유저와 이모티콘 개수에 대해 순회
        for k in range(users_num):
            # 유저가 이모티콘 구매하는데 사용하는 가격
            user_price = 0

            # 이모티콘을 모두 순회하면서
            for j in range(emoji_num):

                # 이모티콘의 할인율이 유저 리스트의 할인율보다 높다면
                if users[k][0] <= new_sales[j]:
                    # 유저가 이모티콘을 구매(할인된 가격)
                    user_price += emoji_price[j] * (100 - new_sales[j]) / 100

                    # 이 때, 구매한 뒤에 유저의 설정된 돈보다 비싸다면
                    if user_price >=  users[k][1]:
                        # plus 가입자의 수를 하나 늘리고 순회에서 탈출. 다음 유저로 이동
                        now_plus += 1
                        break
            # 유저가 플러스에 가입하지 않았다면 -> 수익. 이번 함수에서의 총 가격에 더해줌
            else:
                now_price += user_price

            # 가지치기. 만약 순회중인 유저 리스트에서 남은 유저들이 모두 플러스에 가입하더라도 max값을 넘지 못한다면
            # 그냥 함수를 종료
            if users_num - (k+1) + now_plus < max_plus:
                return
            
        # 모든 유저를 순회하고 난 뒤, max_plus보다 크다면 갱신     
        if max_plus < now_plus:
            max_plus = now_plus
            max_price = now_price

        # max_plus와 현재 함수에서의 플러스 가입자가 같다면 가격 갱신
        elif max_plus == now_plus:
            if max_price < now_price:
                max_price = now_price


    # 아직 이모티콘 할인율을 모두 설정하지 못했다면
    else:
        for j in range(4):
            # 할인율을 설정하고 4번 함수를 호출, 다음 인덱스로 이동
            new_sales[i] = sale_percent[j]
            find_max(i+1, emoji_num, new_sales, emoji_price, users, users_num)


def solution(users, emoticons):
    # 결과로 사용될 변수들 전역변수 선언 및 초기화
    global max_plus
    global max_price
    max_plus = 0
    max_price = 0
    answer = []

    # 길이 구하는 연산을 반복적으로 하지 않기 위해 변수에 저장
    emoji_num = len(emoticons)
    user_num = len(users)

    # 이모티콘의 할인율을 저장할 리스트
    sales_arr = [10] * emoji_num

    # 재귀함수 시작
    find_max(0, emoji_num, sales_arr, emoticons, users, user_num)
    
    answer = [max_plus, max_price]

    return answer
```

#### **😅개선점**

1. 조금 더 가지치기를 잘해서 실행 횟수를 줄일 수 있을 것 같다

### **다른 풀이**

```python
from itertools import product

def solution(users, emoticons):
    E = len(emoticons)
    result = [0, 0]
    percents = (10, 20, 30, 40)
    prod = product(percents, repeat=E)

    for p in prod:
        prod_members, prod_price = 0, 0
        for buy_percent, max_price in users: 
            user_price = 0
            for item_price, item_percent in zip(emoticons, p):
                if item_percent >= buy_percent:
                    user_price += item_price * (100-item_percent) * 0.01

            if user_price >= max_price:
                prod_members += 1
            else:
                prod_price += user_price

        result = max(result, [prod_members, prod_price])

    return result
```

### **🔖정리**

1. 완전탐색

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150368)**<br/>