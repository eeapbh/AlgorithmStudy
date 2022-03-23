
width = 51
height = 37
diagonals = [[17, 19]]

def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1

def solution(width, height, diagonals):
    ans = 0
    tmp = []
    for d in diagonals:
        tmpA1 = [d[0]-1, d[1]]
        tmpA2 = [width-d[0]+1, height - d[1]]
        tmpB1 = [d[0], d[1]-1]
        tmpB2 = [width - d[0], height - d[1]+1]
        tmp = [tmpA1, tmpA2, tmpB1, tmpB2]

        for i in range(0, 4, 2):
            a = factorial(tmp[i][0] + tmp[i][1])//(factorial(tmp[i][0])*factorial(tmp[i][1]))
            b = factorial(tmp[i+1][0] + tmp[i+1][1])//(factorial(tmp[i+1][0])*factorial(tmp[i+1][1]))
            ans += a*b



    return ans%10000019

print(solution(width, height, diagonals))