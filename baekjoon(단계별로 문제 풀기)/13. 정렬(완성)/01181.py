# 1181번(단어 정렬) 문제 : https://www.acmicpc.net/problem/1181
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

S:set = set() # 우선 빈 집합을 만듭니다.

for i in range(N) : 
    S.add(input().rstrip())
    
L:list = list(S) # 집합을 리스트로 변환합니다.
L.sort(key=lambda x : (len(x), x))
# SQL에서 ORDER BY와 비슷한 기능입니다.
# 1순위 : 원소의 길이를 오름차순으로 정렬
# 2순위 : 같은 길이의 원소들 중에서 다시 사전순으로 정렬

for i in range(len(L)) : 
    print(L[i]) # 하나씩 출력합니다.