# 1427번(소트인사이트) : https://www.acmicpc.net/problem/1427
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

numbers:list = []

for i in range(len(str(N))) :
    numbers.append(str(N)[i])
numbers.sort()
numbers.reverse()

result:str = ""
for i in range(len(str(N))) :
    result += numbers[i]
print(result)