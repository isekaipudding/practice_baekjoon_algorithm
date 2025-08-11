# 4153번(직각삼각형) 문제 : https://www.acmicpc.net/problem/4153
import sys

input = sys.stdin.readline

while True :
    A, B, C = map(int, input().split())
    if A==0 and B==0 and C==0 :
        break
    L:list = [A, B, C]
    L.sort()
    if L[0]**2 + L[1]**2 == L[2]**2 :
        print("right")
    else :
        print("wrong")