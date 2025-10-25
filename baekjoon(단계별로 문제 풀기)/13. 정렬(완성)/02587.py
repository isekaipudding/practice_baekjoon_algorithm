# 2587번(대표값2) 문제 : https://www.acmicpc.net/problem/2587
import sys

input = sys.stdin.readline

numbers:list = []
for i in range(5) :
    A:int = int(input().rstrip())
    numbers.append(A)
numbers.sort()
print(int(sum(numbers) / 5))
print(numbers[2])