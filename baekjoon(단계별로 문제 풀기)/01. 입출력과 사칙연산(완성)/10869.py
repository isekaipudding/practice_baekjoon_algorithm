# 10869번(사칙연산) 문제 : https://www.acmicpc.net/problem/10869
import sys

input=sys.stdin.readline

A, B = map(int, input().split())

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)