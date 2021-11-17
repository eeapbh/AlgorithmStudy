import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split(',')))

arr2 = set(arr)

print(arr2)
for i in arr2: