import sys
sys.stdin = open('input.txt', 'r')


arr = {'R':[], "B":[], "Y":[], "G":[]}
arr2 = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
for i in range(5):
    color, number = input().split()
    arr[color].append(int(number))
    arr2[int(number)].append(color)
for v in arr.values():
    v.sort()


def check(arr, arr2):
    # 1 2, 3, 4, 5, 6, 7, 8, 9
    for i in arr.keys():
        if len(arr[i]) == 5:
            if arr[i][0] + arr[i][-1] == arr[i][1] + arr[i][-2] == arr[i][2] * 2:
                return 900 + arr[i][-1]
            else:
                return 600 + arr[i][-1]
    tmp = []

    for k, i in arr2.items():
        tmp.append(len(i))
        if len(i) == 4:
            return 800 + k
    if 3 in tmp:
        for k, v in arr2.items():
            if len(v) == 3:
                three = k
                break

        if 2 in tmp:
            for k, v in arr2.items():
                if len(v) == 2:
                    two = k
                    return three * 10 + two + 700
        else:
            return three + 400
    if tmp.count(2) == 2:
        cnt = 0
        ans = 0
        for k, v in arr2.items():
            if len(v) == 2:
                if cnt == 0:
                    ans = k
                    cnt += 1
                    continue

                if cnt == 1:
                    ans += 10 * k + 300

                    return ans



    if tmp.count(2) == 1:
        for i in arr2.keys():
            if len(arr2[i]) == 2:
                return i + 200

    tmp = []
    for a in arr2.keys():
        if len(arr2[a]) == 1:
            tmp.append(a)
    if tmp[0] + tmp[-1] == tmp[1] + tmp[-2] == tmp[2] * 2:
        return 500 + tmp[-1]

    for i in range(9, 0, -1):
        if len(arr2[i]) == 1:
            return 100 + i
print(arr)
print(arr2)

print(check(arr, arr2))











