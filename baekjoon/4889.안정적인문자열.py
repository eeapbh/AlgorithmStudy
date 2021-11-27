t = 0
while 1:
    t += 1
    line = input()
    if '-' in line:
        break
    stack = []
    cnt = 0
    for i in line:
        if i =='{':
            stack.append('{')
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                cnt += 1
                stack.append('{')


    print(t, end='')
    print('.', cnt + len(stack)//2)
