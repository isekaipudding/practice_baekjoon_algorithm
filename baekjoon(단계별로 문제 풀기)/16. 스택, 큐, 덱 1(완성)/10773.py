# 10773번(제로) 문제 : https://www.acmicpc.net/problem/10773
import sys

input = sys.stdin.readline

stack:list = []

K:int = int(input().rstrip())

for i in range(K) :
    num:int = int(input().rstrip())
    if(num != 0) :
        stack.append(num)
    else :
        stack.pop()
        
result:int = 0

while len(stack) != 0 :
    result += stack.pop()
print(result)