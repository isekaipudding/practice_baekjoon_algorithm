# 11050번(이항 계수 1) 문제 : https://www.acmicpc.net/problem/11050
import sys

input=sys.stdin.readline

N, K = map(int, input().split())

total:int = 1
divide:int = 1
result:int = 1
for i in range(K) :
    total = N-i
    divide = i+1
    result = result * total / divide
    
print(int(result))