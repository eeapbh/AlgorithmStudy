from math import gcd
a, b = map(int, input().split(':'))
x = gcd(a, b)
print('%d:%d' %(a//x, b//x))