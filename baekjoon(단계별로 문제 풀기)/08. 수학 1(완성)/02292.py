# 2292번(벌집) 문제 : https://www.acmicpc.net/problem/2292

import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

if N == 1 : 
    print(1)
elif N > 1 :
    N -= 1
    count:int = 1
    while N > 0 :
        N -= 6 * count
        count += 1
    print(count)