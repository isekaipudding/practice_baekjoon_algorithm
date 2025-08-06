# 11653번(소인수분해) 문제 : https://www.acmicpc.net/problem/11653
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

if N == 1 :
    exit()

factor = 2
while N > 1 :
    if N % factor == 0 :  
        print(factor)  
        N //= factor  
    else :
        factor += 1