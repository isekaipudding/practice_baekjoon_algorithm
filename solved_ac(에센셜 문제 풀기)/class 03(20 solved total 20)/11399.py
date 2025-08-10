# 11399번(ATM) 문제 : https://www.acmicpc.net/problem/11399
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))
L.sort() # 그리디 알고리즘 사용

prefix:list = [0 for _ in range(N)]

# 누적 합 알고리즘 사용
for i in range(len(prefix)) :
    if i == 0 :
        prefix[0] = L[0]
    else :
        prefix[i] = prefix[i-1] + L[i]
        
print(sum(prefix))