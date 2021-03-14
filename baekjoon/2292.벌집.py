# arr = []
# num = 1
# idx = 1
# while 1:
#     arr.append(num)
#     num += 6*idx
#     idx += 1
#     if num > 1000000000:
#         break
# n = int(input())
# arr.append(n)
# arr.sort()
# print(arr.index(n) + 1)

n = int(input())
number = 1
idx = 1
if n == 1:
    print(1)
else:
    while 1:
        number += 6*idx
        if n <= number:
            print(idx + 1)
            break
        idx += 1