# 2480번(주사위 세개) 문제 : https://www.acmicpc.net/problem/2480
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

if A == B and B == C and C == A : 
    print(10000 + A * 1000)
if A == B and B != C and C != A : 
    print(1000 + A * 100)
if A != B and B == C and C != A : 
    print(1000 + B * 100)
if A != B and B != C and C == A : 
    print(1000 + C * 100)
if A != B and B != C and C != A : 
    max:int = A
    if B > max :
        max = B
    if C > max :
        max = C
    print(max * 100)