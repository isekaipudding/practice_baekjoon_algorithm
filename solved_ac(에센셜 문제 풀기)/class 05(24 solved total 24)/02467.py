# 2467번(용액) 문제 : https://www.acmicpc.net/problem/2467
import sys

input = sys.stdin.readline

# 이진 탐색 알고리즘 사용
def binary_search(array, value) :
    START_INDEX, END_INDEX = 0, len(array) - 1
    MIN, MAX = 0, 0
    while START_INDEX < END_INDEX : # 무심코 제가 습관대로 <=로 했군요. 다시 확인하니 <가 맞는 것 같습니다.
        # 투 포인터 알고리즘 사용
        TEMP:int = array[START_INDEX] + array[END_INDEX]
        if abs(TEMP) <= value :
            MIN = array[START_INDEX]
            MAX = array[END_INDEX]
            value = abs(TEMP)
            
        if TEMP <= 0 :
            START_INDEX += 1
        else :
            END_INDEX -= 1
    return MIN, MAX

N:int = int(input().rstrip())
L:list = list(map(int, input().split())) # split()을 빼먹어서 ValueError가 발생했군요!
L.sort() # 이진 탐색 알고리즘을 사용해야 하므로 오름차순으로 정렬

quality_value:int = 10 ** 9 - (- 10 ** 9) # 문제에서 주어진 값의 범위를 참고한 최대 특성값

# 출력 형식을 잘못해서 틀렸군요. 수정합니다.
first, second = binary_search(L, quality_value)
print(first, second)