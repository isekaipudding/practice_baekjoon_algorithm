# 2675번(문자열 반복) 문제 : https://www.acmicpc.net/problem/2675
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    R, S = input().split()
    result:str = ""
    for j in range(len(S)) :
        result += S[j] * int(R)
    print(result)