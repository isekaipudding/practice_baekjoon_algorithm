# 10952번(A+B - 5) 문제 : https://www.acmicpc.net/problem/10952
import sys

input = sys.stdin.readline

while True :
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        break
    print(A + B)