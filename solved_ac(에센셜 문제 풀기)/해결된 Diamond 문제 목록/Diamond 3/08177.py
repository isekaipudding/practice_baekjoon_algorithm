# 8177번(Ice Skates) : https://www.acmicpc.net/problem/8177
import sys

input = sys.stdin.readline

# ─────────────────────────────────────────────────────────────
# Ice Skates — 균일 길이 인터벌(d 고정) + 용량 k
# arr[i] = -K 로 시작, 이벤트 (r, x)에서 arr[r] += x
# 어떤 연속구간 [L..R]의 합 = (#가입자 in [L..R]) - K*(R-L+1)
# 최대 부분배열합 best > K*D  ⇔ 배정 불가(Hall 위배) → "NIE"
# ─────────────────────────────────────────────────────────────

def merge(index, L, R) :
    # 부모 index를 자식 L,R로 갱신
    ssum[index] = ssum[L] + ssum[R]
    # prefix : 왼쪽 prefix vs 왼쪽 합 + 오른쪽 prefix
    pref[index] = pref[L] if pref[L] >= ssum[L] + pref[R] else (ssum[L] + pref[R])
    # suffix : 오른쪽 suffix vs 오른쪽 합 + 왼쪽 suffix
    suff[index] = suff[R] if suff[R] >= ssum[R] + suff[L] else (ssum[R] + suff[L])
    # best : 왼 best, 오른 best, 왼 suffix + 오른 prefix
    b1 = bestv[L]
    b2 = bestv[R]
    b3 = suff[L] + pref[R]
    bestv[index] = b1 if b1 >= b2 and b1 >= b3 else (b2 if b2 >= b3 else b3)

def build(N, K) :
    # 리프 채우기 : 모두 -K
    for i in range(S, S + N) :
        value = -K
        ssum[i] = value
        pref[i] = value
        suff[i] = value
        bestv[i] = value
    # padding 리프(>N)는 -K로 둬도 최대값에 이득이 없으니 안전
    for i in range(S + N, 2 * S) :
        ssum[i] = -K
        pref[i] = -K
        suff[i] = -K
        bestv[i] = -K
    # 내부 노드 빌드
    for i in range(S - 1, 0, -1) :
        L = i << 1
        R = L | 1
        merge(i, L, R)

def point_update(pos_1based, delta) :
    # 리프 위치
    i = S + (pos_1based - 1)
    # 현재 값에 delta 더하고 리프 갱신
    nv = ssum[i] + delta
    ssum[i] = nv
    pref[i] = nv
    suff[i] = nv
    bestv[i] = nv
    # 조상으로 올라가며 병합
    i >>= 1
    while i :
        L = i << 1
        R = L | 1
        merge(i, L, R)
        i >>= 1

N, M, K, D = map(int, input().split())

# 세그트리 크기(2의 거듭제곱)
S = 1
while S < N :
    S <<= 1

# 배열 4개(합/접두/접미/최대부분배열)
ssum  = [0] * (2 * S)
pref  = [0] * (2 * S)
suff  = [0] * (2 * S)
bestv = [0] * (2 * S)

build(N, K)
threshold = K * D

out:list = []
for _ in range(M):
    r, x = map(int, input().split())  # 1 ≤ r ≤ N-D (문제 보장)
    point_update(r, x)
    out.append("NIE" if bestv[1] > threshold else "TAK")

print("\n".join(out))