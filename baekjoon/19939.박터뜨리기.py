n, k = map(int, input().split())

if n < k*(k+1)//2:
    print(-1)
else:
    a = n - k*(k+1)//2
    if a % k == 0:
        print(k-1)
    else:
        print(k)