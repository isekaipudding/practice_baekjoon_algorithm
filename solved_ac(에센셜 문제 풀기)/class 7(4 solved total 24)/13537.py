# 13537번(수열과 쿼리 1) : https://www.acmicpc.net/problem/13537
import sys

input = sys.stdin.readline

# 이진 탐색 알고리즘 사용
def binary_search(array, value) -> int :
    START_INDEX, END_INDEX = 0, len(array)
    while START_INDEX < END_INDEX :
        MID_INDEX = (START_INDEX + END_INDEX) // 2
        if array[MID_INDEX] <= value :
            START_INDEX = MID_INDEX + 1
        else :
            END_INDEX = MID_INDEX
    return START_INDEX

# 세그먼트 트리 빌드
def build(node, start, end) -> None :
    if start == end :
        tree[node] = [L[start]]
    else :
        mid:int = (start + end) // 2
        left, right = node*2, node*2+1
        build(left, start, mid)
        build(right, mid+1, end)
        A, B = tree[left], tree[right]
        # 병합 과정 (merge two sorted lists) <- 머지 소트 알고리즘 사용
        merged:list = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                merged.append(A[i]); i += 1
            else:
                merged.append(B[j]); j += 1
        if i < len(A): merged.extend(A[i:])
        if j < len(B): merged.extend(B[j:])
        tree[node] = merged

# 쿼리 함수
def query(node, start, end, left_q, right_q, k) -> int :
    # 1) 완전 벗어날 때
    if end < left_q or right_q < start:
        return 0
    # 2) 완전 포함될 때
    if left_q <= start and end <= right_q:
        L:list = tree[node]
        # 이진 탐색 사용
        index:int = binary_search(L, k)
        return len(L) - index
    # 3) 일부 겹칠 때
    mid:int = (start + end) // 2
    return (query(node*2,     start,   mid, left_q, right_q, k) +
            query(node*2 + 1, mid + 1, end, left_q, right_q, k))

# 입력 처리
N:int = int(input())
L:list = list(map(int, input().split()))
M:int = int(input())

# 세그먼트 트리 : 각 노드에 정렬된 리스트를 선언
tree:list = [None for _ in range(4 * N)]

# 세그먼트 트리 생성
build(1, 0, N-1)

for _ in range(M) :
    i, j, k = map(int, input().split())
    # 1-based → 0-based
    print(query(1, 0, N-1, i-1, j-1, k))