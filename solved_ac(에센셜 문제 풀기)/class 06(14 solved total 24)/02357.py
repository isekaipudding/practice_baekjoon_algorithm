# 2357번(최솟값과 최댓값) : https://www.acmicpc.net/problem/2357
import sys

input = sys.stdin.readline

def build(data, tree_min, tree_max, node, start, end) :
    if start == end :
        tree_min[node] = data[start]
        tree_max[node] = data[start]
    else :
        mid = (start + end) // 2
        build(data, tree_min, tree_max, 2*node+1, start, mid)
        build(data, tree_min, tree_max, 2*node+2, mid+1, end)
        tree_min[node] = min(tree_min[2*node+1], tree_min[2*node+2])
        tree_max[node] = max(tree_max[2*node+1], tree_max[2*node+2])

def query_min(tree_min, node, start, end, L, R) :
    if end < L or start > R :
        return float('inf')
    if L <= start and end <= R :
        return tree_min[node]
    mid = (start + end) // 2
    left_min = query_min(tree_min, 2*node+1, start, mid, L, R)
    right_min = query_min(tree_min, 2*node+2, mid+1, end, L, R)
    return min(left_min, right_min)

def query_max(tree_max, node, start, end, L, R) :
    if end < L or start > R :
        return float('-inf')
    if L <= start and end <= R :
        return tree_max[node]
    mid = (start + end) // 2
    left_max = query_max(tree_max, 2*node+1, start, mid, L, R)
    right_max = query_max(tree_max, 2*node+2, mid+1, end, L, R)
    return max(left_max, right_max)

# 입력 받기
N, M = map(int, input().split())
L = [int(input().rstrip()) for _ in range(N)]

# 트리 배열 선언
size = 1
while size < N :
    size *= 2
tree_min = [0] * (2 * size)
tree_max = [0] * (2 * size)

# 세그먼트 트리 구축
build(L, tree_min, tree_max, 0, 0, N - 1)

# 쿼리 처리
for _ in range(M) :
    a, b = map(int, input().split())
    MIN = query_min(tree_min, 0, 0, N - 1, a - 1, b - 1)
    MAX = query_max(tree_max, 0, 0, N - 1, a - 1, b - 1)
    print("{} {}".format(MIN, MAX))