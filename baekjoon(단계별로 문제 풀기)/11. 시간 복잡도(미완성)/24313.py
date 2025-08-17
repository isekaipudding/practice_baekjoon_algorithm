# 24313번(알고리즘 수업 - 점근적 표기 1) : https://www.acmicpc.net/problem/24313
import sys

input = sys.stdin.readline

# ax + b <= c * n 형태로 표현
A, B = map(int, input().split())
C:int = int(input().rstrip())
N:int = int(input().rstrip())

if C >= A and A * N + B <= C * N :
    print(1)
else :
    print(0)