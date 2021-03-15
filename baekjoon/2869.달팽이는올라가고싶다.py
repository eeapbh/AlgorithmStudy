# a, b, v = map(int, input().split())
# cnt = ( (v-b) // (a-b) ) - 1
# snail = (a-b) * cnt
# while 1:
#     cnt += 1
#     snail += a
#     if snail >= v:
#         print(cnt)
#         break
#     snail -= b

a,b,v = map(int,input().split())
# k = (v-b)/(a-b)
# print(int(k) if k == int(k) else int(k)+1)

k = (v-b) / (a-b)
if int(k) == k:
    print(int(k))
else:
    print(int(k)+1)