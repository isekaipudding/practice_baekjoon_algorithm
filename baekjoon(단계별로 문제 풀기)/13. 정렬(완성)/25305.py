# 25305번(커트라인) 문제 : https://www.acmicpc.net/problem/25305
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

numbers:list = list(map(int, input().split()))
numbers.sort()

print(numbers[N-K])