n = int(input())
save = [0]*n

for _ in range(n):
    a = int(input())
    if a == 0:
        save.pop()
    else:
        save.append(a)
print(sum(save))