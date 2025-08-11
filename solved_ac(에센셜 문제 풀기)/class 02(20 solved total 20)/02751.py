# 2751번(수 정렬하기 2) 문제 : https://www.acmicpc.net/problem/2751
import sys

input = sys.stdin.readline

T:int=int(input().rstrip())

numbers:list = [0 for _ in range(T)]
for i in range(T) :
    numbers[i] = int(input().rstrip())
numbers.sort()

for i in range(T) :
    print(numbers[i])