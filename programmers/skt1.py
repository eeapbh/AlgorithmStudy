money = 1999
# 1 5 10 50 100 500

costs = [2, 11, 20, 100, 200, 600]
result = 2308

def solution(money, costs):
    coin = [[1], [5], [10], [50], [100], [500]]
    for i in range(6):
        coin[i].append(costs[i])
        coin[i].append(coin[i][1]/coin[i][0])
    print(coin)
    coin.sort(key=lambda x:(x[2], x[0]))
    print(coin)
    ans = 0
    for i in range(6):
        mok = money//coin[i][0]
        money -= mok*coin[i][0]
        ans += coin[i][1]*mok
        if money == 0:
            return ans


print(solution(money, costs))