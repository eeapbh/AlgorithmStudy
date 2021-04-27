# from itertools import permutations
# n = int(input())
# numbers = list(map(int, input().split()))
# info = list(map(int, input().split()))
# operator = ['+', '-', '*', '/']
# operators = []
# for i in range(4):
#     for j in range(info[i]):
#         operators.append(operator[i])
# a = set(permutations(operators))
# a = list(a)
# save = []
# def cal(num, oper, operIdx):
#     if oper == '+':
#         return num + numbers[operIdx+1]
#     elif oper == '-':
#         return num - numbers[operIdx + 1]
#     elif oper == '*':
#         return int(num * numbers[operIdx + 1])
#     elif oper == '/':
#         return int(num / numbers[operIdx + 1])
# for i in range(len(a)):
#     rs = numbers[0]
#     for j in range(len(a[i])):
#         rs = cal(rs, a[i][j], j)
#     save.append(rs)
#
# print(max(save))
# print(min(save))

def cal(num, idx, plus, minus, multi, division):
    global n, MAX, MIN
    if idx == n:
        MAX = max(num, MAX)
        MIN = min(num, MIN)
        return
    else:
        if plus:
            cal(num + numbers[idx], idx+1, plus-1, minus, multi, division)
        if minus:
            cal(num - numbers[idx], idx + 1, plus, minus - 1, multi, division)
        if multi:
            cal(num * numbers[idx], idx + 1, plus, minus, multi - 1, division)
        if division:
            cal(int(num / numbers[idx]), idx + 1, plus, minus, multi, division - 1)

n = int(input())
numbers = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
MAX = -10000000000
MIN = 10000000000
cal(numbers[0], 1, a, b, c, d)
print(MAX)
print(MIN)


