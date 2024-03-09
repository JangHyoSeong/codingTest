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