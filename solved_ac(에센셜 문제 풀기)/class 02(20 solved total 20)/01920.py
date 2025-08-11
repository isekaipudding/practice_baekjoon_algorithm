# 1920번(수 찾기) 문제 : https://www.acmicpc.net/problem/1920
import sys

input = sys.stdin.readline

# 이진 탐색 알고리즘 기초 문제는 13777번(Hunt The Rabbit)
# 해시를 사용한 집합과 맵 기초 문제는 32978번(아 맞다 마늘)

# 다시 확인하니 이 문제는 해시를 사용한 집합과 맵 필요없는 문제이네요.

# 이진 탐색 알고리즘 사용
def binary_search(ARRAY, TARGET):
    START_INDEX = 0
    END_INDEX = len(ARRAY) - 1

    while START_INDEX <= END_INDEX:
        MID_INDEX = (START_INDEX + END_INDEX) // 2

        if ARRAY[MID_INDEX] == TARGET:
            return 1
        elif ARRAY[MID_INDEX] < TARGET:
            START_INDEX = MID_INDEX + 1
        else:
            END_INDEX = MID_INDEX - 1
    return 0  # 존재하지 않는 경우

N:int = int(input().rstrip())
TARGETS:list = list(map(int,input().split()))
TARGETS.sort() # 이진 탐색 알고리즘을 사용할려면 반드시 정렬해야 합니다.

M:int = int(input().rstrip())
SEARCH:list = list(map(int, input().split()))

for i in range(len(SEARCH)) :
    print(binary_search(TARGETS, SEARCH[i]))
    
"""
# 13777번(Hunt The Rabbit) 문제 : https://www.acmicpc.net/problem/13777
import sys

input = sys.stdin.readline

# 이분 탐색 알고리즘 가장 기초적인 문제

def binary_search (array, value):
    START_INDEX, END_INDEX = 1, 50 # 원래 알고리즘은 0, len(array) - 1이나 문제의 조건에 맞게 1, 50으로 수정
    while START_INDEX <= END_INDEX:
        MID_INDEX = (START_INDEX + END_INDEX) // 2
        result.append(MID_INDEX) # 기존 이분 탐색 알고리즘에서 문제의 조건에 맞게 result.append() 추가
        if array[MID_INDEX] == value:
            return MID_INDEX
        if array[MID_INDEX] > value:
            END_INDEX = MID_INDEX - 1
        else:
            START_INDEX = MID_INDEX + 1
    return -1

N:int = 50 # 50 고정
L:list = [i for i in range(N+1)]
L.sort() # 이분 탐색 알고리즘 사용 조건 : 모든 원소들이 오름차순으로 정렬되어 있을 것.

while True :
    value:int = int(input().rstrip())
    if value == 0 :
        break
    
    result:list = []
    binary_search(L, value)
    print(" ".join(map(str, result)))
"""