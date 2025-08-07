# 13548번(수열과 쿼리 6) : https://www.acmicpc.net/problem/13548
import sys
import math
from collections import defaultdict

input = sys.stdin.readline

# 수열과 쿼리 5(13547번)에 있던 모스 알고리즘 코드를 가져와서 해당 문제에 알맞는 형태로 변환합니다.

# 모스 알고리즘 사용
def mo_algorithm(N, L, queries) :
    # 제대로 된 모스 알고리즘을 사용할려면 1순위로 시작 지점들을 제곱근 크기 기준으로 정렬하고 그 다음에 종료 지점을 정렬합니다.
    queries.sort(key=lambda x : (x[1] // block_size, x[2]))
    result:list = [0 for _ in range(len(queries))]

    # 현재 범위의 시작과 끝
    current_left, current_right = 0, 0
    # 찾아 보니 초반에 키가 존재하지 않아 KeyError가 발생했습니다.
    # defaultdict를 import 합니다.
    frequency:dict = defaultdict(int)
    # 수열과 쿼리5에서 current_result의 역할과 비슷합니다.
    max_frequency:int = 0
    # 아무래도 재활용하는 과정에서 count index 범위를 max(L)로 했나 봅니다.
    # 그래서 약 65% 과정에서 max(L) < N일 때 일부 경우에 의해 IndexError가 발생했나 봅니다.
    # 저는 그렇게 추측해보고 N + 1로 수정합니다.
    count:list = [0 for _ in range(N + 1)]

    # 현재 구간에서 원소 하나가 추가되면 해당 숫자에 대하여 count +1 합니다.
    def add(position) :
        nonlocal max_frequency
        element:int = L[position]
        old_count:int = frequency[element]
        frequency[element] += 1
        new_count:int = frequency[element]

        count[old_count] -= 1
        count[new_count] += 1

        if new_count > max_frequency:
            max_frequency = new_count

    # 현재 구간에서 원소 하나가 제거되면 해당 숫자에 대하여 count -1 합니다.
    def remove(position) :
        nonlocal max_frequency
        element:int = L[position]
        old_count:int = frequency[element]
        frequency[element] -= 1
        new_count:int = frequency[element]

        count[old_count] -= 1
        count[new_count] += 1

        if old_count == max_frequency and count[old_count] == 0 :
            max_frequency -= 1

    # 재귀 함수를 통하여 현재 구간에서 한 칸씩 움직입니다.
    for index, left, right in queries :
        while current_right <= right :
            add(current_right)
            current_right += 1
        while current_right > right + 1 :
            current_right -= 1
            remove(current_right)
        while current_left < left :
            remove(current_left)
            current_left += 1
        while current_left > left :
            current_left -= 1
            add(current_left)
        
        result[index] = max_frequency

    return result

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))
T:int = int(input().rstrip())

# 오프라인 쿼리 형식으로 하여 명령어들을 하나의 명령 레지스터에 저장합니다.
query:list = []
for index in range(T) :
    start, end = map(int, input().split())
    query.append((index, start-1, end-1))

# 블록 크기 계산
block_size:int = int(math.sqrt(N))

# 일괄적인 명령어 처리
result:list = mo_algorithm(N, L, query)
for i in range(len(result)) :
    print(result[i])