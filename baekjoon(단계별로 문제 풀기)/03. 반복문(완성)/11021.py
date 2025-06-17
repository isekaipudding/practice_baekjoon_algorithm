# 11021번(A+B - 7) 문제 : https://www.acmicpc.net/problem/11021
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    A, B = map(int, input().split())
    print("Case #{}: {}".format(i+1, A+B))