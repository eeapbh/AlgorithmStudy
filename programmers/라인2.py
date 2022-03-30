sentences = ["ABcD", "bdbc", "a", "Line neWs"]
n = 7
def solution(sentences, n):
    save = []
    score = [0]*(len(sentences))
    for i in range(len(sentences)):
        sc = 0
        for a in sentences[i]:
            if 65<=ord(a)<=90:
                sc += 2
            else:
                sc += 1
        score[i] = sc
    # print(score)

    for s in sentences:
        tmp = set(s)
        if ' ' in tmp:
            tmp.remove(' ')

        newtmp = set()
        for t in tmp:

            if 65<=ord(t)<=90:
                newtmp.add(chr(ord(t) + 32))
                newtmp.add('shift')
            else:
                newtmp.add(t)
        save.append(newtmp)
    print(save)
    keyboard = []
    ans = -123456

    for s in save:
        tmp = 0
        keyboard = s
        for i in range(len(save)):
            for j in save[i]:
                if j in keyboard:
                    continue
                else:
                    break
            else:
                tmp += score[i]
        if tmp > ans:
            ans = tmp




    return ans


print(solution(sentences, n))