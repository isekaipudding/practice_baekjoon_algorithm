# 10818번(최소, 최대) 문제 : https://www.acmicpc.net/problem/10818
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

number:list = list(map(int, input().split()))
MIN:int = number[0]
MAX:int = number[0]

for i in range(N) :
    if MIN > number[i] :
        MIN = number[i]
    if MAX < number[i] :
        MAX = number[i]
            
print("{} {}".format(MIN, MAX))