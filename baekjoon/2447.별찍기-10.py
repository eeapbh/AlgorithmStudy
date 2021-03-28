def draw(arr):
    N = len(arr)
    matrix = []
    for i in range(N * 3):
        if i // N == 1:
            matrix.append(arr[i % N] + " " * N + arr[i % N])
        else:
            matrix.append(arr[i % N] * 3)
    return matrix



star = ['***', '* *', '***']
n = int(input())
e = 0
while n != 3:
    n = n//3
    e += 1

for i in range(e):
    star = draw(star)
for i in star:
    print(i)