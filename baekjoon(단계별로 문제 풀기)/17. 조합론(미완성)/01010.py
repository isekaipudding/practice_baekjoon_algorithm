# 1010번(다리 놓기) 문제 : https://www.acmicpc.net/problem/1010
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    N, M = map(int, input().split())

    total:int = 1
    divide:int = 1
    result:int = 1
    for i in range(N) :
        total = M-i
        divide = i+1
        result = result * total / divide
        
    print(int(result))