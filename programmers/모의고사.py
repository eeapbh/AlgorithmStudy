def solution(answers):
    n = len(answers)
    save = [0, 0, 0, 0]
    answer = []
    arr1, arr2, arr3 = [], [], []
    while 1:
        arr1 += [1, 2, 3, 4, 5]
        if len(arr1) > n:
            break
    while 1:
        arr2 += [2, 1, 2, 3, 2, 4, 2, 5]
        if len(arr2) > n:
            break
    while 1:
        arr3 += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        if len(arr3) > n:
            break
    for i in range(n):
        if answers[i] == arr1[i]:
            save[1] += 1
        if answers[i] == arr2[i]:
            save[2] += 1
        if answers[i] == arr3[i]:
            save[3] += 1
    for s in range(1, 4):
        if save[s] == max(save):
            answer.append(s)
    print(arr1)
    print(arr2)
    print(save)
    return answer

answers = [1, 2, 3, 4, 5]
print(solution(answers))