# 10951번(A+B - 4) 문제 : https://www.acmicpc.net/problem/10951
import sys

input = sys.stdin.readline

while True :
    try :
        A, B = map(int,input().split())
        print(A + B)
    except :
        break