board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

def solution(board, skill):
    answer = 0
    for s in skill:
        if s[0] == 1:
            for i in range(s[1], s[3]+1):
                for j in range(s[2], s[4]+1):
                    board[i][j] -= s[5]
        elif s[0] == 2:
            for i in range(s[1], s[3]+1):
                for j in range(s[2], s[4]+1):
                    board[i][j] += s[5]

    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 1:
                board[i][j] = 1
            if board[i][j]<1:
                board[i][j] = 0
    memo = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            memo[i][j] = board[i - 1][j - 1] + memo[i][j - 1] + memo[i - 1][j] - memo[i - 1][j - 1]
    answer = (memo[n][m] - memo[0][m] - memo[n][0] + memo[0][0])


    return answer

print(solution(board, skill))

