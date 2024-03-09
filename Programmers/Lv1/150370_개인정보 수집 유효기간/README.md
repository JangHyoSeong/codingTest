# 문제 제목
개인정보 수집 유효기간
## **📝문제 설명**
고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.

다음은 오늘 날짜가 2022.05.19일 때의 예시입니다.

|약관 종류|	유효기간|
|:--:|:--:|
|A|	6 |달|
|B|	12|달|
|C|	3 |달|

|번호|개인정보 수집 일자|약관 종류|
|:--:|:--:|:--:|
|1|2021.05.02|A|
|2|2021.07.01|B|
|3|2022.02.19|C|
|4|2022.02.20|C|


- 첫 번째 개인정보는 A약관에 의해 2021년 11월 1일까지 보관 가능하며, 유효기간이 지났으므로 파기해야 할 개인정보입니다.
- 두 번째 개인정보는 B약관에 의해 2022년 6월 28일까지 보관 가능하며, 유효기간이 지나지 않았으므로 아직 보관 가능합니다.
- 세 번째 개인정보는 C약관에 의해 2022년 5월 18일까지 보관 가능하며, 유효기간이 지났으므로 파기해야 할 개인정보입니다.
- 네 번째 개인정보는 C약관에 의해 2022년 5월 19일까지 보관 가능하며, 유효기간이 지나지 않았으므로 아직 보관 가능합니다.  

따라서 파기해야 할 개인정보 번호는 [1, 3]입니다.

오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다. 이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
### **⚠제한사항**
나머지는 링크 참조

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def solution(today, terms, privacies):
    answer = []

    today_year ,today_month, today_day = map(int, today.split('.'))

    term_dict = {}
    for term in terms:
        term_name, term_month = term.split()
        term_dict[term_name] = int(term_month)

    for i in range(len(privacies)):
        privacy_date, privacy_term = privacies[i].split()
        year, month, day = map(int, privacy_date.split('.'))
        month -= 1

        add_month = term_dict[privacy_term]
        year = year + (month + add_month) // 12
        month = (month + add_month) % 12 + 1

        if year < today_year:
            answer.append(i+1)

        elif year == today_year:

            if month < today_month:
                answer.append(i+1)

            elif month == today_month:
                if day <= today_day:
                    answer.append(i+1)

    return answer
```

### **다른 풀이**

```python
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
```

## 📚참고 사이트

- **🔗[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150370)**<br/>