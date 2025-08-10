# 18870번(좌표 압축) 문제 : https://www.acmicpc.net/problem/18870
import sys

input = sys.stdin.readline

# 이진 탐색 알고리즘 사용
def binary_search(array, value) :
    START_INDEX, END_INDEX = 0, len(array) - 1
    while START_INDEX <= END_INDEX :
        MID_INDEX = (START_INDEX + END_INDEX) // 2
        if array[MID_INDEX] == value :
            return MID_INDEX # 여기서는 index 값을 반환합니다.
        elif array[MID_INDEX] < value :
            START_INDEX = MID_INDEX + 1
        else :
            END_INDEX = MID_INDEX - 1
    return -1

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))

# 값/좌표 압축 작업 실행
SET_AND_SORTED:list = sorted(set(L))

result:list = []

for i in range(N) :
    index:int = binary_search(SET_AND_SORTED, L[i])
    result.append(index)
    
print(" ".join(map(str, result)))