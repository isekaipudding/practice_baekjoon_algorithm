# 13925번(수열과 쿼리 13) 문제 : https://www.acmicpc.net/problem/13925
import sys

input = sys.stdin.readline

MOD = 10 ** 9 + 7

# 세그먼트 트리를 만듭니다.
def build(start, end, index) :
    if start == end :
        tree[index] = L[start]
        return
    mid = (start + end) // 2
    build(start, mid, index * 2)
    build(mid + 1, end, index * 2 + 1)
    tree[index] = (tree[index * 2] + tree[index * 2 + 1]) % MOD

def push_down(index, start, end) :
    if start != end:
        for child in [index * 2, index * 2 + 1] :
            # lazy의 곱셈과 덧셈을 각각 적용
            lazy[child][0] = (lazy[child][0] * lazy[index][0]) % MOD
            lazy[child][1] = (lazy[child][1] * lazy[index][0]) + lazy[index][1]
            lazy[child][1] %= MOD
    # 현재 노드의 값을 업데이트
    tree[index] = (tree[index] * lazy[index][0] + lazy[index][1] * (end - start + 1)) % MOD
    # lazy 배열 초기화
    lazy[index][0] = 1
    lazy[index][1] = 0

# 1번 명령어, 2번 명령어, 3번 명령어를 수행할 함수입니다.
# 지연 전파(느리게 갱신되는 세그먼트 트리) 알고리즘 사용
def update_range(start_range, end_range, value, cmd, start, end, index) :
    push_down(index, start, end)
    if end_range < start or start_range > end :
        return
    if start_range <= start and end <= end_range:
        if cmd == 1:
            # 덧셈 추가
            lazy[index][1] = (lazy[index][1] + value) % MOD
        elif cmd == 2:
            # 곱셈 적용
            lazy[index][0] = (lazy[index][0] * value) % MOD
            lazy[index][1] = (lazy[index][1] * value) % MOD
        else:
            # 값 대입
            lazy[index][0] = 0
            lazy[index][1] = value % MOD
        push_down(index, start, end)
        return
    mid = (start + end) // 2
    update_range(start_range, end_range, value, cmd, start, mid, index * 2)
    update_range(start_range, end_range, value, cmd, mid + 1, end, index * 2 + 1)
    tree[index] = (tree[index * 2] + tree[index * 2 + 1]) % MOD

# 4번 명령어를 실행할 함수입니다.
# 구간 합 구하기 2(10999번) 소스 코드를 참고했습니다.
def query_sum(start_range, end_range, start, end, index):
    push_down(index, start, end)
    if end_range < start or start_range > end:
        return 0
    if start_range <= start and end <= end_range:
        return tree[index] % MOD
    mid = (start + end) // 2
    left_sum = query_sum(start_range, end_range, start, mid, index * 2)
    right_sum = query_sum(start_range, end_range, mid + 1, end, index * 2 + 1)
    return (left_sum + right_sum) % MOD

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))
T:int = int(input().rstrip())

# 이번엔 배열 크기를 더 크게 만듭니다.
# 여유분을 고려하여 N -> N+1로 설정합니다.
tree:list = [0] * (4 * (N+1))
# lazy 배열을 두개로 하고, [곱셈, 덧셈]으로 관리하는 구조
lazy:list = [[1, 0] for _ in range(4 * (N+1))]

# 최초 트리 빌드
build(0, N-1, 1)

for _ in range(T):
    query:list = list(map(int, input().split()))
    cmd:int = query[0]
    # cmd 1,2,3 형태가 모두 동일하므로 조건문을 이렇게 설정합니다.
    if 1 <= cmd and cmd <= 3 :
        # 연산 요청
        start_index = query[1] - 1
        end_index = query[2] - 1
        value = query[3]
        update_range(start_index, end_index, value, cmd, 0, N-1, 1)
    elif cmd == 4 :
        # 구간 합 요청
        start_index = query[1] - 1
        end_index = query[2] - 1
        result = query_sum(start_index, end_index, 0, N-1, 1)
        print(result % MOD)