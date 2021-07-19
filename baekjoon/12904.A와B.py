a = list(input())
b = list(input())
while 1:
    if len(a) == len(b):
        break
    if b[-1] == 'A':
        b.pop()
        continue
    if b[-1] == 'B':
        b.pop()
        b.reverse()
        continue
if a == b:
    print(1)
else:
    print(0)



