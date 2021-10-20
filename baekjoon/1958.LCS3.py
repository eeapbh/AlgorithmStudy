a = input()
b = input()
c = input()
n1 = len(a)
n2 = len(b)
n3 = len(c)


dp = [[[0]*n3 for _ in range(n2)] for _ in range(n1)]

def LCS(x, y, z):

    if x < 0 or b < 0 or c < 0:
        return 0
    if dp[x][y][z] == -1:
        dp[x][y][z] = 0

        if a[x] == b[y] == c[z]:
            dp[x][y][z] = LCS(x-1, y-1, z-1) + 1
        else:
            dp[x][y][z] = max(max(LCS(x, y-1, z), LCS(x-1, y, z)), LCS(x, y, z-1))

    return dp[x][y][z]

print(LCS(n1-1, n2-1, n3-1))