# 15552번(빠른 A+B) 문제 : https://www.acmicpc.net/problem/15552
import sys

input=sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    A, B = map(int,input().split())
    print(A + B)