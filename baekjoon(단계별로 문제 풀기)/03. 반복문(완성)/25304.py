# 25304번(영수증) 문제 : https://www.acmicpc.net/problem/25304
import sys

input = sys.stdin.readline

price:int = int(input().rstrip())
T:int = int(input().rstrip())

sum:int = 0
for i in range(T) :
    unit, N = map(int, input().split())
    sum += unit*N

if price == sum :
    print("Yes")
else :
    print("No")