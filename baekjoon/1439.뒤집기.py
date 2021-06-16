line = list(map(int, input()))
trg = line[0]
cnt0 = 0
cnt1 = 0
if trg == 0:
    cnt0 += 1
else:
    cnt1 += 1
for i in line:
    if i != trg:
        trg = i
        if trg == 0:
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))

