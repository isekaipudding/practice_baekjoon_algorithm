# 10999번(구간 합 구하기 2) 문제 : https://www.acmicpc.net/problem/10999
import sys

input = sys.stdin.readline

# 구간 합 구하기 1(2042번) 문제에서 느리게 갱신되는 세그먼트 트리 알고리즘(지연 전파)을 사용한 것입니다.
# 일일히 타이핑 하기엔 시간이 너무 오래 걸려 ChatGPT의 도움을 받았습니다.

# build 함수 (구간 합 저장)
def build_sum(data, tree, index, start, end) :
    if start == end :
        tree[index] = data[start]
    else :
        mid = (start + end) // 2
        build_sum(data, tree, 2*index, start, mid)
        build_sum(data, tree, 2*index+1, mid+1, end)
        tree[index] = tree[2*index] + tree[2*index+1]

# update_range 함수
def update_range(tree, lazy, index, start, end, range_start, range_end, value) :
    # 선행 업데이트 : 필요 시 현재 노드를 업데이트
    if lazy[index] != 0 :
        tree[index] += (end - start + 1) * lazy[index]
        if start != end:
            lazy[2*index] += lazy[index]
            lazy[2*index+1] += lazy[index]
        lazy[index] = 0
        
    # 범위를 벗어난 경우
    if end < range_start or start > range_end :
        return

    # 범위 내인 경우 완전히 덮기
    if range_start <= start and end <= range_end :
        tree[index] += (end - start + 1) * value
        if start != end :
            lazy[2*index] += value
            lazy[2*index+1] += value
        return

    # 그렇지 않은 경우, 자식으로 내려감
    mid = (start + end) // 2
    update_range(tree, lazy, 2*index, start, mid, range_start, range_end, value)
    update_range(tree, lazy, 2*index+1, mid+1, end, range_start, range_end, value)
    tree[index] = tree[2*index] + tree[2*index+1]

# query_sum 함수 (구간 합 계산)
def query_sum(tree, lazy, index, start, end, L, R) :
    # 선행 업데이트
    if lazy[index] != 0 :
        tree[index] += (end - start + 1) * lazy[index]
        if start != end :
            lazy[2*index] += lazy[index]
            lazy[2*index+1] += lazy[index]
        lazy[index] = 0

    # 범위를 벗어난 경우
    if R < start or end < L :
        return 0

    # 완전히 포함된 경우
    if L <= start and end <= R :
        return tree[index]

    # 아니면 자식으로 내려가서 계산
    mid = (start + end) // 2
    left_sum = query_sum(tree, lazy, 2*index, start, mid, L, R)
    right_sum = query_sum(tree, lazy, 2*index+1, mid+1, end, L, R)
    return left_sum + right_sum

# 데이터 입력
N, K, M = map(int, input().split())
L = [int(input().rstrip()) for _ in range(N)] # 이렇게 입력하는게 더 나은 것 같습니다.

# 세그먼트 트리 크기 계산
size = 1
while size < N :
    size *= 2

# 트리 구조와 지연 배열
tree_sum = [0] * (2 * size)
lazy = [0] * (2 * size)

# 초기 트리 빌드
build_sum(L, tree_sum, 1, 0, N-1)

# 쿼리 처리
for _ in range(K + M) :
    query = list(map(int, input().split()))
    cmd = query[0]
    if cmd == 1 :
        # 범위 값 변경
        update_start_index = query[1] - 1
        update_end_index = query[2] - 1
        value = query[3]
        update_range(tree_sum, lazy, 1, 0, N-1, update_start_index, update_end_index, value)
    elif cmd == 2 :
        # 구간 합 구하기
        start_index = query[1] - 1
        end_index = query[2] - 1
        # 여기서 lazy를 빼먹어서 TypeError 발생
        result = query_sum(tree_sum, lazy, 1, 0, N-1, start_index, end_index)
        print(result)