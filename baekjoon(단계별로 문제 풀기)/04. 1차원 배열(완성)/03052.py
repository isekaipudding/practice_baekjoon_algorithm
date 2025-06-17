# 3052번(나머지) 문제 : https://www.acmicpc.net/problem/3052
import sys

input = sys.stdin.readline

check:list = [False for _ in range(42)]
number:list = [0 for _ in range(10)]

for i in range(10) :
    number[i] = int(input().rstrip())
    number[i] %= 42
    check[number[i]] = True
    
count:int = 0
for i in range(42) :
    if check[i] == True :
        count += 1

print(count)