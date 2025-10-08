# 28262번(초콜릿 비긴즈) : https://www.acmicpc.net/problem/28262
import sys

input = sys.stdin.readline

MOD:int = 10**9 + 7

# 에디토리얼 : https://u.acmicpc.net/4cc6c91c-4a1b-4333-a52c-736f17d890e9/chococup2.pdf

# ----------------------------------------------------------------------
# [H. 초콜릿 비긴즈 - 에디토리얼 요약 및 본 코드의 준수 사항]
# 1. 일반성: N <= M으로 두고, N <= 3 일 때만 비트 DP를 돌린다.
#    N >= 4 에서는 답이 커지지 않고 반복(4-주기) 성질을 이용한다. (에디토리얼)
# 2. 비트 DP 상태 :
#    - 가로 길이 l, 마지막 두 열 패턴 p1, p2(비트마스크), 전체 흰색 수 k.
#    - 수직 3연속(한 열 내부), 수평/대각 3연속(최근 3열 조합) 금지.
#    - 가능한 열 집합과 (p1,p2)->p3 전이를 전처리하여 실제 전이만 돈다. (N=3이면 전이 총 28개 수준)
# 3. N >= 4 의 구조적 성질 :
#    - 비긴 보드의 중간 2x2마다 흑/백이 2:2로 분할되어야 하며,
#      특정 패턴이 한 번 등장하면 상하좌우로 유일하게 확장되는 반복 패턴이 된다.
# 4. N, M >= 5 이면 모든 비긴 보드가 위 패턴을 포함 → 답은 항상 8 이하이며
#    (N mod 4, M mod 4)만으로 결정된다. 따라서 5..8 대표 크기를 비트 DP로 전부 미리 구하고,
#    임의의 (N,M)은 (5 + (N-5)%4, 5 + (M-5)%4)로 매핑해 값을 취한다.
# 5. N = 4 예외 :
#    - 4 x M (M >= 5) 의 답은 14 (M과 무관)
#    - 4 x 4 의 답은 18
# 6. 이 코드는 위 원칙들을 그대로 구현 :
#    - valid_columns: 세로 3연속 제거
#    - ok_triple: 최근 3열에 대한 수평/대각 3연속 금지 검사
#    - solve_by_dp: 흰색 개수 == ceil(N*M/2) 인 경우만 합산
#    - solve: N>=5는 대표(5..8)로 매핑, N=4 예외 분기, N<=3은 DP
# ----------------------------------------------------------------------

# 6. 이 프로그램은 4개의 함수를 바탕으로 구현되었습니다.

# 2. 비트 DP 상태 - 세로 3연속 금지 구현부
def valid_columns(n: int):
    # 세로줄(한 열) 비트마스크 중 '세로 3연속'이 없는 것만 반환
    cols:list = []
    for m in range(1 << n) :
        ok:bool = True
        if n >= 3 :
            for r in range(n - 2):
                b0 = (m >> r) & 1
                b1 = (m >> (r + 1)) & 1
                b2 = (m >> (r + 2)) & 1
                # 같은 색(0 or 1)으로 세 칸 연속이면 금지
                if b0 == b1 == b2:
                    ok = False
                    break
        if ok :
            cols.append(m)
    return cols

# 2. 비트 DP 상태 - 최근 3열 가로/대각 3연속 금지 구현부
def ok_triple(m1: int, m2: int, m3: int, n: int) -> bool :
    # 최근 3열 (m1,m2,m3)에서 가로/대각 3연속이 생기지 않는지 검사
    mask_all:int = (1 << n) - 1
    # 가로 3연속 금지: 같은 행에서 m1==m2==m3 금지(0,0,0 / 1,1,1 모두 배제)
    fail_mask:int = ~((m1 ^ m2) | (m2 ^ m3)) & mask_all
    if fail_mask :
        return False
    if n >= 3 :
        # 대각 ↘
        for r in range(n - 2) :
            if ((m1 >> r) & 1) == ((m2 >> (r + 1)) & 1) == ((m3 >> (r + 2)) & 1) :
                return False
        # 대각 ↗
        for r in range(n - 2) :
            if ((m1 >> (r + 2)) & 1) == ((m2 >> (r + 1)) & 1) == ((m3 >> r) & 1) :
                return False
    return True

# 2. 전이 전처리: 가능한 (p1,p2)->p3 조합만 보관해서 실제 전이만 수행
def precompute_trresultitions(n: int) :
    # 2. 가능한 세로줄과 (m1,m2)->m3 전이들을 전처리
    cols:list = valid_columns(n)
    S:int = len(cols)
    pc:list = [c.bit_count() for c in cols]  # 각 열의 흰색(1)의 개수
    trresult:list = [[[] for _ in range(S)] for _ in range(S)]
    for i, m1 in enumerate(cols) :
        for j, m2 in enumerate(cols) :
            lst = []
            for k, m3 in enumerate(cols) :
                if ok_triple(m1, m2, m3, n) :
                    lst.append(k)
            trresult[i][j] = lst
    return cols, pc, trresult

def solve_by_dp(n: int, m: int) -> int :
    """
    n x m 보드의 '비긴 최종 보드' 개수 (흰색 수 = ceil(nm/2))를 DP로 계산
    - n <= 8, m <= 1000까지 커버 (n>=5, m>=5는 작은 대표값으로 대체해서 사용)
    - 상태: (마지막 두 열의 인덱스 쌍, 누적 흰색 수)
    """
    cols, pc, trresult = precompute_trresultitions(n)
    S:int = len(cols)
    # (2. 흰색 수를 정확히 ceil(N*M/2)로 고정)
    Ktarget:int = (n * m + 1) // 2

    # (2. DP 기저: m == 1, 2 처리)
    if m == 1 :
        return sum(1 for i in range(S) if pc[i] == Ktarget) % MOD
    if m == 2 :
        ret:int = 0
        for i in range(S) :
            for j in range(S) :
                if pc[i] + pc[j] == Ktarget :
                    ret += 1
        return ret % MOD

    # 2. 초기 상태: l=2, (p1,p2) 쌍별로 누적 흰색 수 카운트
    pair_count:int = S * S
    dp:list = [[0] * (Ktarget + 1) for _ in range(pair_count)]
    active:list = []
    for i in range(S):
        for j in range(S):
            w = pc[i] + pc[j]
            if w <= Ktarget:
                dp[i * S + j][w] = 1
                active.append(i * S + j)

    # 2. 상태 전이: 전처리된 trresult를 사용하여 열 3..m 확장
    for col in range(3, m + 1) :
        prev_maxw:int = min(Ktarget, n * (col - 1))
        new_dp:list = [[0] * (Ktarget + 1) for _ in range(pair_count)]
        new_active:set = set()
        for pair in active :
            i, j = divmod(pair, S)
            L:list = dp[pair]
            for k in trresult[i][j] :
                pop = pc[k]
                dest = j * S + k
                out = new_dp[dest]
                # L[t] -> out[t + pop] (누적 흰색 수 이동)
                limit2 = min(prev_maxw, Ktarget - pop)
                if limit2 >= 0 :
                    if pop == 1 :
                        for t in range(limit2, -1, -1) :
                            v = L[t]
                            if v :
                                out[t + 1] = (out[t + 1] + v) % MOD
                    elif pop == 2 :
                        for t in range(limit2, -1, -1) :
                            v = L[t]
                            if v :
                                out[t + 2] = (out[t + 2] + v) % MOD
                    else :
                        for t in range(limit2, -1, -1) :
                            v = L[t]
                            if v :
                                out[t + pop] = (out[t + pop] + v) % MOD
                new_active.add(dest)
        dp = new_dp
        active = list(new_active)

    result:int = 0
    for pair in active :
        result = (result + dp[pair][Ktarget]) % MOD
    return result

def solve(N: int, M: int) -> int:
    # 1. 일반성 : N <= M 으로 정규화
    n, m = (N, M) if N <= M else (M, N)
    
    # 3. N >= 4인 경우 특정 패턴이 한 번 등장하면 상하좌우로 유일하게 확장되는 반복 패턴이 됩니다.
    # 3. 그 안에서 N >= 5인 경우와 N == 4인 경우로 분리됩니다.(많은 조건 분기)

    # 4. N >= 5 : 4주기 성질 → 5..8 대표에 매핑 (답은 8 이하, (N mod 4, M mod 4)로 결정)
    if n >= 5:
        # 5..8 전 범위 작은 DP 사전 계산
        result8:dict = {}
        for nn in range(5, 9):
            for mm in range(5, 9):
                result8[(nn, mm)] = solve_by_dp(nn, mm)
        nrep:int = 5 + (n - 5) % 4
        mrep:int = 5 + (m - 5) % 4
        return result8[(nrep, mrep)]

    # 5. N = 4 : 예외 상수 (4xM(M>=5)=14, 4x4=18)
    if n == 4 :
        if m == 4 :
            return 18
        else:
            return 14

    # 1. N <= 3 : 그대로 DP
    return solve_by_dp(n, m)

N, M = map(int, input().rstrip().split())
print(solve(N, M) % MOD)