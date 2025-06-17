# 10950번(A+B - 3) 문제 : https://www.acmicpc.net/problem/10950
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    A, B = map(int,input().split())
    print(A + B)