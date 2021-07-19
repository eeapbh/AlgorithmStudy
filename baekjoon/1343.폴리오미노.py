# line = input()
# save = []
# cnt1 = 0
# cnt2 = 0
# for i in range(len(line)):
#     if line[i] == 'X':
#         if cnt2 != 0:
#             save.append(['.', cnt2])
#         cnt1 += 1
#         cnt2 = 0
#         if i == len(line) - 1:
#             save.append(['X', cnt1])
#
#     else:
#         if cnt1 != 0:
#             save.append(['X', cnt1])
#         cnt2 += 1
#         cnt1 = 0
#         if i == len(line) - 1:
#             save.append(['.', cnt2])
#
# ans = ''
# for s in save:
#     if s[0] == 'X':
#         a = s[1] // 4
#         b = s[1] % 4
#         ans += 'AAAA' * a
#         if b == 0 or b == 2:
#             ans += b * 'B'
#         else:
#             print(-1)
#             exit()
#     if s[0] == '.':
#         ans += s[1] * '.'
# print(ans)
board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)

