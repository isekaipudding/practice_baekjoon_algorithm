# 2903번(중앙 이동 알고리즘) 문제 : https://www.acmicpc.net/problem/2903
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

LineLength:int = 2 #초기 상태의 한 변의 점의 개수
for i in range(N) :
    LineLength *= 2
    LineLength -= 1
print(LineLength ** 2)