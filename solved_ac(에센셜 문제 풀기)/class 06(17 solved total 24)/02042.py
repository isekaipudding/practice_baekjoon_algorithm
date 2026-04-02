# 2042번(구간 합 구하기) : https://www.acmicpc.net/problem/2042
import sys

input = sys.stdin.readline

# 수열과 쿼리 16(14428번) 문제의 소스 코드에서 조금 변형한 것입니다.

# 데이터 입력
N, K, M = map(int, input().split())
L = [int(input().rstrip()) for _ in range(N)]

# 세그먼트 트리 크기 계산
size = 1
while size < N :
    size *= 2

# 트리 구조: 합을 저장
tree_sum = [0] * (2 * size)

# build 함수 (구간 합 저장)
def build_sum(data, tree, index, start, end) :
    if start == end :
        tree[index] = data[start]
    else :
        mid = (start + end) // 2
        build_sum(data, tree, 2*index, start, mid)
        build_sum(data, tree, 2*index+1, mid+1, end)
        tree[index] = tree[2*index] + tree[2*index+1]

# update 함수
def update_sum(tree, index, start, end, update_index, value) :
    if start == end :
        tree[index] = value
    else :
        mid = (start + end) // 2
        if update_index <= mid :
            update_sum(tree, 2*index, start, mid, update_index, value)
        else :
            update_sum(tree, 2*index+1, mid+1, end, update_index, value)
        tree[index] = tree[2*index] + tree[2*index+1]

# query_sum 함수 (구간 합 계산)
def query_sum(tree, index, start, end, L, R) :
    if R < start or end < L :
        return 0
    if L <= start and end <= R :
        return tree[index]
    mid = (start + end) // 2
    left_sum = query_sum(tree, 2*index, start, mid, L, R)
    right_sum = query_sum(tree, 2*index+1, mid+1, end, L, R)
    return left_sum + right_sum

# 초기 빌드
build_sum(L, tree_sum, 1, 0, N-1)

# 쿼리 처리
for _ in range(K + M) :
    query = list(map(int, input().split()))
    cmd = query[0]
    if cmd == 1 :
        # 값 변경
        update_index = query[1] - 1
        value = query[2]
        update_sum(tree_sum, 1, 0, N-1, update_index, value)
    elif cmd == 2 :
        # 구간 합 구하기
        start_index = query[1] - 1
        end_index = query[2] - 1
        result = query_sum(tree_sum, 1, 0, N-1, start_index, end_index)
        print(result)