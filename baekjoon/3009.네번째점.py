arr1 = []
arr2 = []
for _ in range(3):
    x, y = map(int, input().split())
    arr1.append(x)
    arr2.append(y)
for i in arr1:
    if arr1.count(i) == 1:
        print(i, end=' ')
        break
for i in arr2:
    if arr2.count(i) == 1:
        print(i, end=' ')
        break
