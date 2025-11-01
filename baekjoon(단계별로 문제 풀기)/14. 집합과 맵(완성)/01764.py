# 1764번(듣보잡) 문제 : https://www.acmicpc.net/problem/1764
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# set 자료구조 사용
non_hear:set = set() # 듣도 못한 사람
non_see:set = set() # 보도 못한 사람

for i in range(N) :
    non_hear.add(input().rstrip())
for i in range(M) :
    non_see.add(input().rstrip())

nobody:set = non_hear.intersection(non_see) # 듣보잡
result:list = sorted(nobody)

print(len(result))
for i in range(len(result)) :
    print(result[i])