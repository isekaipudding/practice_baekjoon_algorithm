# 10872번(팩토리얼) 문제 : https://www.acmicpc.net/problem/10872
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

result:int = 1

for i in range(1, N+1, 1) :
    result *= i
print(result)