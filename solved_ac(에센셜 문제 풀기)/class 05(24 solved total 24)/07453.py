# 7453번(합이 0인 네 정수) 문제 : https://www.acmicpc.net/problem/7453
import sys

input = sys.stdin.readline

def solve(L) :
    a:list = L[0]
    b:list = L[1]
    c:list = L[2]
    d:list = L[3]
    x:dict = dict()
    
    for i in a :
        for j in b :
            t = i + j
            x[t] = x.get(t,0) + 1
    result:int = 0
    for i in c :
        for j in d :
            t = - i - j
            result += x.get(t,0)
    return result

T:int = int(input().rstrip())
L:list = [[0 for _ in range(T)] for _ in range(4)]

for i in range(T) :
    L[0][i], L[1][i], L[2][i], L[3][i] = map(int,input().rstrip().split())
    
    
print(solve(L))