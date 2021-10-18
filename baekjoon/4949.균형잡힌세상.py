def check(line):
    stack = []
    for i in line:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                return 'no'
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
        elif i == ']':
            if not stack:
                return 'no'
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'

while 1:
    line = input()
    if line == '.':
        break
    print(check(line))
