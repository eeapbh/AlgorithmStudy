import sys
sys.stdin = open('input.txt', 'r')
accumulation={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
def md_to_d(month, day):
    return accumulation[month]+day
flowers=[]
N=int(sys.stdin.readline())
for i in range(N):
    start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split())
    flowers.append((md_to_d(start_month, start_day), md_to_d(end_month, end_day)))
selected=[]
start=0
end=60
startdate=60
enddate=334
flowers.sort(key=lambda x:(x[0], x[1]))
x=-1
temp=0
changed=0
selected=[]
while end<=enddate and x<N:
    changed=0
    x+=1
    for i in range(x, N):
        if flowers[i][0]>end:
            break
        if temp<flowers[i][1]:
            temp=flowers[i][1]
            x=i
            changed=1
    if changed==1:
        end=temp
        selected.append(flowers[x])
    else:
        selected=[]
        break
print(len(selected))
