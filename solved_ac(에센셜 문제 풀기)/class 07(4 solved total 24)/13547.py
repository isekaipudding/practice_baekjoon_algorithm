# 13547번(수열과 쿼리 5) : https://www.acmicpc.net/problem/13547
import sys
import math

input = sys.stdin.readline

# 모스 알고리즘 사용
def mo_algorithm(L, queries) :
    # 제대로 된 모스 알고리즘을 사용할려면 1순위로 시작 지점들을 제곱근 크기 기준으로 정렬하고 그 다음에 종료 지점을 정렬합니다.
    queries.sort(key=lambda x : (x[1] // block_size, x[2]))
    result:list = [0 for _ in range(len(queries))]

    # 현재 범위의 시작과 끝
    current_left, current_right = 0, 0
    current_result:int = 0
    count:list = [0 for _ in range(max(L) + 1)]

    # 중복되지 않는 새로운 데이터 들어오면 하나 추가하거나, 이미 있다면 count +1 합니다.
    def add(position) :
        nonlocal current_result
        element:int = L[position]
        count[element] += 1
        if count[element] == 1 :
            current_result += 1

    # 구간에서 하나 제거될 때 count -1 하거나, count == 1 마지막으로 제거되면 중복되지 데이터 목록에서 제거합니다.
    def remove(position) :
        nonlocal current_result
        element:int = L[position]
        if count[element] == 1 :
            current_result -= 1
        count[element] -= 1

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
        
        result[index] = current_result

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
result:list = mo_algorithm(L, query)
for i in range(len(result)) :
    print(result[i])