t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(input())
    arr2 = list(input())
    d = 0
    for i in range(n):
        if arr1[i] != arr2[i]:
            d += 1
    x = abs(arr1.count('W') - arr2.count('W'))
    print(x + (d-x)//2)
