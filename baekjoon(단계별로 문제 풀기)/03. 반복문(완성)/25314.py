# 25314번(코딩은 체육과목 입니다) 문제 : https://www.acmicpc.net/problem/25314
import sys
import math

input = sys.stdin.readline

N:int = int(input().rstrip())

result = ""
for i in range(math.ceil(N/4)) : 
    result += "long "
result += "int"
print(result)