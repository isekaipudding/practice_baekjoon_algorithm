# 10871번(X보다 작은 수) 문제 : https://www.acmicpc.net/problem/10871
import sys

input = sys.stdin.readline

N, X = map(int, input().split())

number:list = list(map(int, input().split()))
result:list = []

if len(number) >= N :
    for i in range(N) :
        if(number[i] < X) :
            result.append(number[i])
            
print(" ".join(map(str, result)))