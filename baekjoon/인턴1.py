cards =[[10, 5, 15], [5, 15, 10], [10, 11, 9]]

def solution(cards):
    n = len(cards)
    check = [0]*n
    ans = 0
    for i in range(n):
        if check[i] == 1:
            continue
        for j in range(i+1, n):
            m1 = min(cards[i])
            m2 = min(cards[j])
            a = cards[i].index(min(cards[i]))
            b = cards[j].index(min(cards[j]))
            if a == b:
                continue
            cards[i][a] += 1
            cards[i][b] -= 1
            cards[j][b] += 1
            cards[j][a] -= 1
            check[i] = 1
            check[j] = 1
            m3 = min(cards[i])
            m4 = min(cards[j])
            if m1 >= m3 or m2 >= m4:
                cards[i][a] -= 1
                cards[i][b] += 1
                cards[j][b] -= 1
                cards[j][a] += 1
                check[i] = 0
                check[j] = 0

            break
    for c in cards:
        ans += min(c)

    return ans

print(solution(cards))