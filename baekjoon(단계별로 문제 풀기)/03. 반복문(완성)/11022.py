# 11022번(A+B - 8) 문제 : https://www.acmicpc.net/problem/11022
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))