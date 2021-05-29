arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = []
tmp = list(zip(*arr))
for i in tmp:
    arr2.append(i[::-1])
print(arr2)