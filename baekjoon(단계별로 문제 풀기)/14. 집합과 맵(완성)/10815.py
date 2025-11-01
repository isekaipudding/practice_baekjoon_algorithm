# 10815번(숫자 카드) 문제 : https://www.acmicpc.net/problem/10815
import sys

input = sys.stdin.readline

# 시간 복잡도 log N 보장해주는 이진 탐색 알고리즘입니다!
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

RESULTS:list = []
for i in range(len(SEARCH)) :
    RESULTS.append(binary_search(TARGETS, SEARCH[i]))
    
print(" ".join(map(str, RESULTS)))