t = int(input())
stack = []
for _ in range(t):
    info = input()
    ans = 0
    for i in info:
        if i == '[':
            stack.append(i)
        else:
            ans = max(len(stack), ans)
            stack.pop()

    print(2**ans)
