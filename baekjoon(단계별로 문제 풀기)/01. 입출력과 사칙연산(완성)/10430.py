# 10430번(나머지) 문제 : https://www.acmicpc.net/problem/10430
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

print((A + B) % C)
print((A%C + B%C) % C)
print(A * B % C)
print((A%C) * (B%C) % C)