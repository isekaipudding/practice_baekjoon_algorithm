# 5086번(배수와 약수) 문제 : https://www.acmicpc.net/problem/5086
import sys

input = sys.stdin.readline

while True :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break
    if N < M and M % N == 0 :
        print("factor")
    elif N > M and N % M == 0 :
        print("multiple")
    else :
        print("neither")