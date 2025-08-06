# 2501번(약수 구하기) 문제 : https://www.acmicpc.net/problem/2501
import sys

input = sys.stdin.readline

# 원래 다른 알고리즘이 존재하나 브루트 포스 알고리즘으로 풀라고 했으니 이 방식으로 풀어봅니다.

N, K = map(int, input().split())

numbers:list = []
for i in range(1, N+1) :
    if N%i == 0 :
        numbers.append(i)

if len(numbers) >= K :
    print(numbers[K-1])
else :
    print(0)