# 13334번(철로) : https://www.acmicpc.net/problem/13334
import sys
import heapq

input = sys.stdin.readline

N:int = int(input().rstrip())
L:list[tuple[int, int]] = []

# 각 사람마다 집(home)과 사무실(office) 좌표가 주어질 때
# 이 사람은 [집, 사무실] 구간 어딘가에 철로를 깔아주면 출퇴근할 수 있다고 봅니다.
# 즉, 이 사람은 선분 [min(home, office), max(home, office)] 로 표현 가능합니다.
for _ in range(N) :
    home, office = map(int, input().split())
    L.append((min(home, office), max(home, office)))

D:int = int(input().rstrip()) # 설치할 수 있는 철로의 길이

"""
[핵심 아이디어]
철로의 길이가 D로 고정일 때,
한 위치에 [x, x + D] 구간을 깔았다고 하자.
이 구간 안에 "완전히 포함"되는 근로자 구간 [start, end] 의 수를 최대화하고 싶다.

즉, end ≤ x + D  그리고 start ≥ x <=> start ≥ end - D
[결론]
어떤 사람의 구간 끝점 end를 '오른쪽 끝'으로 맞추고,
왼쪽 끝이 [end - D, end] 안에 있는 사람들만 센다.

그러면 "end 기준으로 오름차순으로 훑으면서"
현재 end보다 D 이상 왼쪽으로 벗어나는(start < end - D) 구간은 버리고
그 안에 남아있는 구간 수의 최댓값을 구하면 된다.

이걸 위해 우리는 사람 구간을 end 기준으로 정렬하고,
"현재 고려 중인 end"와 함께 유지할 수 있는 start들을 최소 힙으로 관리한다.
힙에서 가장 작은 start가 현 end에서 너무 멀면(pop) 버림.
"""

# 사람 구간을 끝점(end) 기준으로 오름차순 정렬
# (같은 end라면 start가 작은 순)
L.sort(key=lambda x: (x[1], x[0]))

# TEMP는 현재 힙에서 가장 왼쪽(가장 작은 start)을 추적하기 위한 보조 변수처럼 쓰고 있습니다.
# 아래 로직에서 TEMP가 반드시 있어야 하는 건 아니지만,
# 작성자가 "이전 최소 start + D로 현재 end를 커버 가능한가?"를 가볍게 체크하려고 둔 것.
# L이 비어있지 않다는 전제(N>=1)에서 초기화.
TEMP:int = L[0][0]

heap:list[tuple[int, int]] = [] # 최소 힙
# 파이썬 heapq는 최소 힙.
# 여기서는 (start, end) 자체를 넣어 봅니다.
# 그러면 heap[0][0]이 항상 가장 작은 start가 됩니다.

result:int = 0 # 설치 가능한 철로로 커버 가능한 최대 사람 수


for i in range(N) :
    start, end = L[i]

    # 만약 이 사람의 구간 길이 자체가 D보다 크면,
    # 이 사람은 어떤 철로 길이 D로도 절대 한 번에 커버할 수 없습니다.
    # (철로가 그 사람 구간 전체를 못 덮음)
    if end - start > D :
        continue

    # 이 사람을 후보에 넣습니다.
    # 지금 보고 있는 end를 오른쪽 끝으로 생각했을 때,
    # start가 충분히 오른쪽이면(즉 end-D 이상이면) 유지될 것이고,
    # 너무 왼쪽이면 나중에 pop.
    heapq.heappush(heap, L[i]) # (start, end)
    """
    이제 힙에 든 사람들 중에서,
    현재 end 기준으로 더 이상 커버 불가능한(너무 왼쪽에 있는) 사람들은 제외합니다.
    
    커버 조건은 start >= end - D.
    그 반대인 start < end - D 를 만족하면 그 사람은 못 태운다 -> pop
    
    아래 while문은 heap[0]의 start가 end-D보다 작은 동안 계속 제거합니다.
    """
    if end > TEMP + D:
        while heap and heap[0][0] + D < end:
            # heap[0][0] + D < end
            # <=> heap[0][0] < end - D
            # 즉 이 사람은 현재 end 기준으로 커버 불가 -> 제거
            heapq.heappop(heap)

    # TEMP를 현재 힙에서 가장 작은 start로 갱신합니다.
    TEMP = heap[0][0]

    # 현재 힙에 남아있는 사람 수가
    # "길이 D의 철로 하나로 동시에 커버 가능한 최대 인원 수" 후보가 됩니다.
    result = max(result, len(heap))

# 최종 출력
print(result)