# 10816번(숫자 카드 2) 문제 : https://www.acmicpc.net/problem/10816
from collections import defaultdict
import bisect
import sys

input = sys.stdin.readline

# N을 입력 받음
N = int(input().rstrip())

# N개의 정수를 입력 받아 리스트 L1 생성
L1 = list(map(int, input().split()))

# M을 입력 받음
M = int(input().rstrip())

# M개의 정수를 입력 받아 리스트 L2 생성
L2 = list(map(int, input().split()))

# L1의 원소를 세어 사전 D 생성
D = defaultdict(int)
for number in L1:
    D[number] += 1

# D의 key들을 정렬하여 sorted_keys 리스트 생성
sorted_keys = sorted(D.keys())

# result 리스트 초기화
result = []

# 이분 탐색을 통해 각 L2의 원소를 검사
for query in L2:
    # query가 있는지 확인
    index = bisect.bisect_left(sorted_keys, query)
    
    # query가 sorted_keys에 존재하는지 검사
    if index < len(sorted_keys) and sorted_keys[index] == query:
        result.append(D[query])  # 존재하면 value를 추가
    else:
        result.append(0)  # 존재하지 않으면 0을 추가

# 결과 출력
print(" ".join(map(str, result)))