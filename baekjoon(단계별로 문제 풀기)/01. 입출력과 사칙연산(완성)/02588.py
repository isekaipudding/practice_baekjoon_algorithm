# 2588번(곱셈) 문제 : https://www.acmicpc.net/problem/2588
import sys

input = sys.stdin.readline

A:int = int(input().rstrip())
B:int = int(input().rstrip())

one:int = B // 10**0 % 10
ten:int = B // 10**1 % 10
hundred:int = B // 10**2 % 10

print(A * one)
print(A * ten)
print(A * hundred)
print(A * B)