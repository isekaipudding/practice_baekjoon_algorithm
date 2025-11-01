# 10816번(숫자 카드 2) 문제 : https://www.acmicpc.net/problem/10816
import sys

input = sys.stdin.readline

# 복습하는 중입니다.

# 이진 탐색 알고리즘 사용
def binary_search(array, value) :
    START_INDEX, END_INDEX = 0, len(array)-1
    while START_INDEX <= END_INDEX :
        MID_INDEX = (START_INDEX + END_INDEX) // 2
        if array[MID_INDEX] == value :
            return True
        elif array[MID_INDEX] < value :
            START_INDEX = MID_INDEX + 1
        else :
            END_INDEX = MID_INDEX -1
    return False

# 입력하기
N:int = int(input().rstrip())
L1:list = list(map(int, input().split()))
M:int = int(input().rstrip())
L2:list = list(map(int, input().split()))

# L1의 원소들을 중복 없이 오름차순으로 정렬한 후 리스트에 저장합니다.
sorted_keys:list = sorted(set(L1))

# 사전으로 해당 key가 몇 개 있는지 value로 저장합니다.
# 예시로 L1=[1,1,2,3]이면 D={1:2, 2:1, 3:1}로 저장됩니다.
D:dict = dict()
# 모든 key에 대한 value를 0으로 초기화합니다.
for i in range(len(sorted_keys)) :
    D[sorted_keys[i]] = 0
# 해당 key가 존재하면 그 key의 value에 1을 더합니다.
for i in range(len(L1)) :
    D[L1[i]] += 1

result:list = []
for i in range(len(L2)) :
    # 만약 해당 key가 존재하면 해당 key의 value를 추가
    if binary_search(sorted_keys, L2[i]) :
        result.append(D[L2[i]])
    # 만약 해당 key가 존재하지 않으면 0 추가
    else :
        result.append(0)

print(" ".join(map(str, result)))

"""
# 혹은 이렇게 만들어도 됩니다.
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
"""