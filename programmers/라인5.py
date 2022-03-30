abilities =[7, 6, 8, 9, 10]
k = 1

def solution(abilities, k):
    ans = 0
    abilities.sort()
    n = len(abilities)
    while abilities:
        if len(abilities) == 1:
            if k > 0:
                ans += abilities[0]
                break
            else:
                break
        a = abilities.pop()
        b = abilities.pop()
        if a - b == 0:
            ans += b
        if a > b:
            if n % 2 == 1:
                if a - b > abilities[0]:
                    if k > 0:
                        k -= 1
                        ans += a
                else:
                    ans += b
            elif n % 2 == 0:
                if k > 0:
                    ans += a
                    k -=1


    return ans

print(solution(abilities, k))