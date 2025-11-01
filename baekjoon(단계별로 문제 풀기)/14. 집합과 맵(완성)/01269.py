# 1269번(대칭 차집합) 문제 : https://www.acmicpc.net/problem/1269
import sys

input = sys.stdin.readline

M, N = map(int, input().split()) # 배열의 크기를 정해주는 것으로 파이썬에서는 필요없는 입력
A:set = set(list(map(int, input().split())))
B:set = set(list(map(int, input().split())))
print(len(A.union(B)) - len(A.intersection(B)))