while True:
    string = input()
    if string == ".":
        break

    flag = True
    stack = []
    for c in string:
        if c in ["[", "("]:
            stack.append(c)

        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break

        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    
    if stack:
        flag = False
    
    print("yes" if flag else "no")