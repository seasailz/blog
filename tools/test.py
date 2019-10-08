# _*_ coding: utf-8 _*_
__date__ = '2019/10/7 16:01'

import math
import pprint


# n = 0
# for m in range(101, 201, 2):
#     k = int(math.sqrt(m))
#     for i in range(2, k+2):
#         if m % i == 0:
#             break
#     if i == k + 1:
#         if n % 10 == 0:
#             print()
#         print('%d' % m, end=' ')
#         n += 1

# n = int(input('行数：'))
# for i in range(0, n):
#     for j in range(0, 10-i):
#         print(' ', end='')
#     for j in range(0, 2*i-1):
#         print('*', end='')
#     print()

# from math import *
# print('三位数中所有水仙花数为：')
# for i in range(100, 1000):
#     n1 = i // 100
#     n2 = (i % 100) // 10
#     n3 = i % 10
#     if pow(n1, 3) + pow(n2, 3) + pow(n3, 3) == i:
#         print(i, end=' ')

# print('1~1000所有的完数有，其因子为：')
# for n in range(6, 1001):
#     total = 0
#     factors = []
#     for i in range(1, n):
#         if n % i == 0:
#             factors.append(i)
#             total += i
#     if total == n:
#         print('{0}:{1}'.format(n, factors))

m = int(input('请输入整数 m：'))
n = int(input('请输入整数 n：'))
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print(m)
