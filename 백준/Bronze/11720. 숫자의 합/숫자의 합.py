# 숫자의 합


import sys
input = sys.stdin.readline


n = int(input())
lst = input()

sum_v = 0
for i in range(n):
    sum_v += int(lst[i])

print(sum_v)
