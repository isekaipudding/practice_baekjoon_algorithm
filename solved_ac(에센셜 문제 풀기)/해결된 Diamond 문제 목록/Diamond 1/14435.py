# 14435번(놀이기구 2) 문제 : https://www.acmicpc.net/problem/14435
import sys
import heapq

input = sys.stdin.readline

def read_n_ints(n: int) -> list :
    values:list = []
    while len(values) < n :
        values += list(map(int, input().split()))
    return values

N, M, K, Q = map(int, input().split())
limits:list = [0] + read_n_ints(M) # 1-based
grow:list = read_n_ints(K)         # day 1..K에 성장하는 아이

U:list     = [0 for _ in range(Q)]
V:list     = [0 for _ in range(Q)]
LIMIT:list = [0 for _ in range(Q)]

heaps:list   = [[] for _ in range(N + 1)]
checked:list = [0 for _ in range(Q)]

push = heapq.heappush
pop = heapq.heappop

for qid in range(Q) :
    u, v, k = map(int, input().split())
    U[qid] = u
    V[qid] = v
    LIMIT[qid] = limits[k]

    thread:int = (LIMIT[qid] + 1) // 2
    if u == v :
        push(heaps[u], (thread, qid))
    else :
        push(heaps[u], (thread, qid))
        push(heaps[v], (thread, qid))

height:list = [0 for _ in range(N + 1)]

result_prev2 = 0 # result[day-2]
result_prev  = 0 # result[day-1]

for day in range(1, K + 1, 1) :
    result:int = result_prev

    kid:int   = grow[day - 1]
    delta:int = 1
    if day >= 3 and result_prev > result_prev2 :
        delta = 2

    height[kid] += delta
    hk = height[kid]
    hp = heaps[kid]

    while hp and hp[0][0] <= hk :
        thread, qid = pop(hp)
        if checked[qid] :
            continue

        u = U[qid]
        v = V[qid]
        limit = LIMIT[qid]

        if u == v :
            if 2 * height[u] >= limit :
                checked[qid] = 1
                result += 1
            else :
                deficit = limit - 2 * height[u]
                add = (deficit + 1) // 2
                push(heaps[u], (height[u] + add, qid))
        else :
            if height[u] + height[v] >= limit :
                checked[qid] = 1
                result += 1
            else :
                deficit = limit - (height[u] + height[v])
                add = (deficit + 1) // 2
                push(heaps[u], (height[u] + add, qid))
                push(heaps[v], (height[v] + add, qid))

    print(result)
    result_prev2, result_prev = result_prev, result