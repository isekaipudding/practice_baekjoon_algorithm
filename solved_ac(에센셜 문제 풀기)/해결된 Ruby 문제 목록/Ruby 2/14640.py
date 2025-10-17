# 14640번(Scenery) 문제 : https://www.acmicpc.net/problem/14640
import sys
import heapq

# 에디토리얼 : https://icpc.global/worldfinals/problems/2017-ICPC-World-Finals/finals2017solutions.pdf
# 참고 소스 코드 : https://github.com/hijkl2e/problem_solving/blob/main/boj/Volume%2014/boj14640.cpp
# 시간 복잡도를 O(N^2) -> O(N log N)으로 개선을 위해 kcm1700님의 소스 코드를 참고했습니다. 와 이렇게 구현되는구나...ㄷㄷ

# ------------------------------------------------------------
# 에디토리얼 2안 기반: "브랜칭 + idle 상태 1개만 유지"
# - 퍼시스턴트 이항 힙(Persistent Binomial Heap) : 전역 arena(list) + 함수들만 사용
# - 힙들을 세그트리로 묶어 구간 병합(build() 사용)
# - 이벤트 타임라인(map 대체) : 최소 힙으로 동적 삽입/처리
# 클래스 없이 def만으로 구성합니다.
# ------------------------------------------------------------

sys.setrecursionlimit(1 << 25)

input = sys.stdin.readline

# Arena (persistent) - 전역
arena:list[tuple[int,list[int]]] = []  # 각 노드는 (key:int, children:list[int]) 튜플로 저장

def arena_push(key, children) :
    """노드를 arena에 추가하고 인덱스를 반환."""
    arena.append((key, children))
    return len(arena) - 1

# -------------------------
# Persistent Min Binomial Heap (by indices) - 함수형
# heap은 '루트들의 node 인덱스 리스트'로 표현
# -------------------------
def heap_empty(roots) :
    return not roots

def heap_min_key(roots) :
    """힙의 최소 key 조회 (빈 힙이면 0 반환; 호출 전 empty 검사 권장)"""
    if not roots :
        return 0
    m = roots[0]
    mk = arena[m][0]
    for r in roots[1:] :
        rk = arena[r][0]
        if rk < mk:
            m = r
            mk = rk
    return mk

def _meld_same_order(ai, bi):
    """같은 차수(자식 수)의 트리 ai, bi 병합 → 새 노드 인덱스."""
    ak, ach = arena[ai]
    bk, bch = arena[bi]
    if ak <= bk :
        # 새 루트: ai의 key, 자식: [bi] + ai.children
        return arena_push(ak, [bi] + ach)
    else:
        return arena_push(bk, [ai] + bch)

def heap_meld(A, B) :
    """이항 힙 병합. roots 리스트 두 개를 받아 새 roots 반환."""
    i = j = 0
    carry = -1
    out = []
    # 차수(=children 길이) 기준으로 같은 차수끼리만 병합
    while i < len(A) or j < len(B) or carry != -1 :
        min_order = 10**30
        cand = []
        ri = A[i] if i < len(A) else -1
        rj = B[j] if j < len(B) else -1
        if ri != -1 :
            min_order = min(min_order, len(arena[ri][1]))
        if rj != -1 :
            min_order = min(min_order, len(arena[rj][1]))
        if carry != -1 :
            min_order = min(min_order, len(arena[carry][1]))
        if ri != -1 and len(arena[ri][1]) == min_order :
            cand.append(ri)
        if rj != -1 and len(arena[rj][1]) == min_order :
            cand.append(rj)
        if carry != -1 and len(arena[carry][1]) == min_order :
            cand.append(carry)

        if len(cand) == 1 :
            r = cand[0]
            out.append(r)
            if r == ri: i += 1
            if r == rj: j += 1
            if r == carry: carry = -1
            continue

        if len(cand) == 3 :
            # 셋이면 하나는 결과로 내리고, 나머지 둘 병합 → carry
            r = cand[2]
            out.append(r)
            if r == ri: i += 1
            if r == rj: j += 1
            if r == carry: carry = -1

        a, b = cand[0], cand[1]
        if a == ri: i += 1
        if a == rj: j += 1
        if a == carry: carry = -1
        if b == ri: i += 1
        if b == rj: j += 1
        if b == carry: carry = -1
        carry = _meld_same_order(a, b)
    return out

def heap_insert(roots, key) :
    """키 하나를 삽입한 새 힙 반환."""
    node = arena_push(key, [])
    return heap_meld(roots, [node])

def _min_root_position(roots) :
    if not roots :
        return -1
    best = 0
    bk = arena[roots[0]][0]
    for i in range(1, len(roots)) :
        rk = arena[roots[i]][0]
        if rk < bk:
            best = i
            bk = rk
    return best

def heap_delete_min(roots) :
    """최소 루트를 제거한 새 힙 반환."""
    position = _min_root_position(roots)
    if position == -1 :
        return []
    min_root = roots[position]
    result = roots[:position] + roots[position+1:]
    # 자식들로 서브 힙 구성 (역순)
    childs = arena[min_root][1]
    sub = list(reversed(childs))
    return heap_meld(result, sub)

# 세그트리(힙 저장, 구간 병합) - build() 사용
def build(leaf_heaps) :
    """
    leaf_heaps: 길이 N, 각 원소는 '힙 roots(list[int])'
    반환: (segment, base)  where  segment는 길이 2*base, base는 리프 시작 인덱스
    """
    n = len(leaf_heaps)
    base = 1
    while base < n :
        base <<= 1
    segment = [[] for _ in range(2 * base)]  # 빈 힙은 [] 로 표현
    for i in range(n):
        segment[base + i] = leaf_heaps[i]
    for i in range(base - 1, 0, -1):
        segment[i] = heap_meld(segment[i << 1], segment[(i << 1) | 1])
    return segment, base

def segment_range_meld(segment, base, l, r, seed) :
    """세그트리에서 [l, r] 구간의 힙을 모두 병합해 seed 힙에 반영."""
    if l > r :
        return seed
    L = base + l
    R = base + r
    result = seed
    while L <= R:
        if (L & 1) == 1:
            result = heap_meld(result, segment[L])
            L += 1
        if (R & 1) == 0:
            result = heap_meld(result, segment[R])
            R -= 1
        L >>= 1; R >>= 1
    return result

n, t = map(int, input().split())
n:int; t:int  # -------------- [static type]

pairs:list[tuple[int,int]] = [tuple(map(int, input().split())) for _ in range(n)]
pairs.sort()  # (a, b) 시작 오름차순

# idle 상태
idle_heap:list[int] = []     # PHeap roots
idle_rel:int = 0             # 다음으로 등장할 작업 인덱스
idle_take:int = 0            # 시작한 사진 수
idle_ok:bool = True          # 항상 유효

# 세그트리 리프: 각 항목의 마감만 담은 힙
leafs:list[list[int]] = [[] for _ in range(n)]
for i in range(n) :
    leafs[i] = heap_insert([], pairs[i][1])
segment, base = build(leafs)
segment:list[list[int]]; base:int  # -------------- [static type]

# 이벤트 타임라인(우선순위 큐) + 상태 테이블
timeline:list[int] = []
in_queue:set[int] = set()
states:dict[int,dict[str,object]] = {}  # time -> dict(heap, rel, take, ok)

# 시작시각 키들 초기 삽입
for i in range(n) :
    a = pairs[i][0]
    a:int  # -------------- [static type]
    if a not in states :
        states[a] = {"heap": [], "rel": 0, "take": 0, "ok": False}
    if a not in in_queue :
        heapq.heappush(timeline, a)
        in_queue.add(a)

index_release:int = 0
last_add:tuple[int,int] = (-1, -1)  # (count, min_deadline)

while timeline :
    current = heapq.heappop(timeline)
    current:int  # -------------- [static type]

    st = states.get(current)
    if st is not None and st["ok"] and st["take"] >= idle_take :
        # st.heap + [st.rel .. idle_rel-1] 리프 힙 병합 → idle 갱신
        merged = st["heap"]
        merged:list[int]  # -------------- [static type]
        if st["rel"] < idle_rel :
            merged = segment_range_meld(segment, base, st["rel"], idle_rel - 1, merged)
        idle_heap = merged
        idle_take = st["take"]
        last_add = (-1, -1)

    # current에 새로 열리는 항목을 idle 힙에 삽입
    while index_release < n and pairs[index_release][0] == current :
        idle_heap = heap_insert(idle_heap, pairs[index_release][1])
        index_release += 1
    idle_rel = index_release

    # 시작 가능한가? (EDF)
    if not heap_empty(idle_heap) :
        earliest = heap_min_key(idle_heap)
        earliest:int  # -------------- [static type]
        worth = (last_add[0] < idle_take + 1) or (last_add[0] == idle_take + 1 and last_add[1] > earliest)
        worth:bool  # -------------- [static type]
        if current + t <= earliest and worth :
            next_time = current + t
            next_time:int  # -------------- [static type]
            next = states.get(next_time)
            if next is None :
                next = {"heap": [], "rel": 0, "take": 0, "ok": False}
                states[next_time] = next
            if (not next["ok"]) or (idle_take + 1 >= next["take"]) :
                last_add = (idle_take + 1, earliest)
                next["heap"] = heap_delete_min(idle_heap)
                next["rel"]  = idle_rel
                next["take"] = idle_take + 1
                if next["take"] == n :
                    print("yes")
                    sys.exit(0)
                next["ok"] = True
                if next_time not in in_queue :
                    heapq.heappush(timeline, next_time)
                    in_queue.add(next_time)

print("no")