arr = list(input())
stack = []
is_valid = True

for bracket in arr:
    # 여는 괄호는 스택에 삽입
    if bracket == '(' or bracket == '[':
        stack.append(bracket)
    
    # 닫는 괄호라면
    else:
        # 스택이 비어있다면 올바르지 않은 괄호입력
        if not stack:
            is_valid = False
            break
        
        # 스택의 맨 위 값을 pop
        top = stack.pop()
        
        # 만약 여는괄호, 닫는괄호가 제대로 쌍이 맞다면
        if (bracket == ')' and top == '(') or (bracket == ']' and top == '['):
            # ()인 경우 값은 2, []인 경우 값은 3
            value = 2 if bracket == ')' else 3
            # 스택의 최상위가 숫자인 경우, 값을 누적한다.
            if stack and isinstance(stack[-1], int):
                value += stack.pop()
            stack.append(value)
        elif isinstance(top, int):
            if not stack:
                is_valid = False
                break
            opening_bracket = stack.pop()
            if (bracket == ')' and opening_bracket != '(') or (bracket == ']' and opening_bracket != '['):
                is_valid = False
                break
            multiplier = 2 if bracket == ')' else 3
            value = top * multiplier
            # 스택의 최상위가 숫자인 경우, 값을 누적한다.
            if stack and isinstance(stack[-1], int):
                value += stack.pop()
            stack.append(value)
        else:
            is_valid = False
            break

# 최종 값 계산
total_value = 0
for item in stack:
    if isinstance(item, int):
        total_value += item
    else:
        is_valid = False

if is_valid:
    print(total_value)
else:
    print(0)
