# 2739번(구구단) 문제 : https://www.acmicpc.net/problem/2739
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

for i in range(1, 10) :
    print("{} * {} = {}".format(N, i, N * i))