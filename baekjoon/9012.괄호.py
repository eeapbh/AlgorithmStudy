n = int(input())
for _ in range(n):
    line = input()
    stack = []
    for i in line:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print('NO')
                break
            stack.pop()
    else:
        if len(stack) > 0:
            print('NO')
        else:
            print('YES')

