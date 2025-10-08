# 20027번(LCS 8) : https://www.acmicpc.net/problem/20027
import sys

input = sys.stdin.readline

# 참고 소스 코드가 따로 있긴 한데 그 소스 코드 참고해도 Python에서 TLE가 계속 발생합니다.
# PyPy3으로 겨우 뚫었습니다! 이걸로 제가 최초로 LCS 8 문제를 Python으로 해결하였습니다. 와... 너무 어렵다.
# 이제 남는 것은 단 하나! LCS 9 뿐입니다. LCS 9만 해결하면 LCS 시리즈 모두 해결!

MOD:int = 10**9 + 7
ALPHABET:int = 26

S:str = input().rstrip()
K:int = int(input().rstrip())
N:int = len(S)

# 패딩 과정
SP:str = "###" + S + "###"
L:int = len(SP)

# 윈도우(길이 7) 내 문자 -> 7비트 마스크를 만들기 위해
# 각 위치의 알파벳 비트를 미리 계산
def letter_index(ch) :
    o:int = ord(ch) - 65
    return o if 0 <= o < 26 else -1

# ---- (1) 전처리 : NEXT[j][mask] 만들기 ----
# mask 비트로 계산
# j는 [0..255] 중 하나, mask는 [0..127] 중 하나. 불가능은 -1로 둡니다.
NEXT:list = [[-1]*128 for _ in range(256)]

def trresult(j, mask) :
    # 참고 소스 코드에서 solve()의 prefix_lcs_base/current_lcs를 그대로 재현 (prefix_lcs_base은 8칸, current_lcs는 차이 누적)
    # prefix_lcs_base[0] = (j >> 6) - 1
    # prefix_lcs_base[i] = prefix_lcs_base[i-1] + ((j >> (6 - i)) & 1), i=1..6 ; prefix_lcs_base[7]은 0으로 둠(원 코드 관행)
    prefix_lcs_base:list = [0]*8
    prefix_lcs_base[0] = (j >> 6) - 1
    for i in range(1, 7) :
        prefix_lcs_base[i] = prefix_lcs_base[i-1] + ((j >> (6 - i)) & 1)
    # current_lcs는 직전값만 필요
    current_lcs_prev:int = 0
    next_state:int = 0
    current_lcs_at_4 = None
    # i = 1..7 (윈도우 왼쪽부터 오른쪽으로)
    for i in range(1, 8) :
        bit:int = (mask >> (i - 1)) & 1  # i-1 위치가 매치면 1
        if bit :
            current_lcs_i = prefix_lcs_base[i-1] + 1
        else :
            # else : max(prefix_lcs_base[i], current_lcs[i-1])
            vi = prefix_lcs_base[i] if i < 8 else 0
            current_lcs_i = vi if vi > current_lcs_prev else current_lcs_prev
        if i == 4 :
            current_lcs_at_4 = current_lcs_i
        transition_bit = current_lcs_i - current_lcs_prev
        next_state = (next_state << 1) + transition_bit
        current_lcs_prev = current_lcs_i
    # LCS>=3(= current_lcs[4] >= 3) 조건 미달이면 -1 (은 0 상태로 보냈지만, 다음 단계에서 무시되도록)
    if current_lcs_at_4 is None or current_lcs_at_4 < 3:
        return -1
    return next_state  # 0..127

for j in range(256) :
    for m in range(128) :
        NEXT[j][m] = trresult(j, m)

# ---- (2) DP 준비 ----
# 시작 상태 : dp[1][64*K + 56] = 1
start_j:int = 64*K + 56
dp:list = [0]*256
dp[start_j] = 1
active:list = [start_j]  # 활성 상태만 순회

# ---- (3) 본 DP : N 스텝 ----
# 각 스텝 i(=패딩 포함 인덱스 3..L-4)에서
#  - 윈도우 SP[i-3..i+3] 에 대해 '등장 문자들의 7비트 마스크'를 만들고
#  - 부재 묶음(others) = 26 - disttransition_bit
#  - mask=0(others) 1회 + 등장 문자들(<=7개) 각각 1회만 전이
for i in range(3, L-3) :
    # 윈도우의 문자별 7비트 마스크
    masks:list = [0]*ALPHABET
    w:list = SP[i-3:i+4]  # 길이 7
    for t, ch in enumerate(w):
        index:int = letter_index(ch)
        if index >= 0:
            masks[index] |= (1 << t)
    # disttransition_bit, others
    disttransition_bit:int = 0
    for m in masks :
        if m :
            disttransition_bit += 1
    others:int = ALPHABET - disttransition_bit

    # 다음 DP
    next_dp:list = [0]*256
    next_active:list = []

    # 전이 함수
    def push_mask(mask, multi) :
        if multi == 0 :
            return
        # 활성 상태만 순회
        for j in active :
            value = dp[j]
            if not value :
                continue
            k = NEXT[j][mask]
            # k가 [56..255]만 다음 단계에서 사용되므로, 그 미만은 무시해도 동일
            if k >= 56 :
                if next_dp[k] == 0 :
                    next_active.append(k)
                next_dp[k] = (next_dp[k] + value * multi) % MOD

    # others 묶음(매치 없는 글자들) : mask=0
    if others :
        push_mask(0, others)

    # 실제 등장한 문자들만
    for index in range(ALPHABET) :
        m = masks[index]
        if m :
            push_mask(m, 1)

    dp = next_dp
    # 중복 제거(짧은 리스트니까 set 변환이 더 빠를 때가 많음)
    if next_active :
        active = list(set(next_active))
    else :
        active = []

# 정답 : 마지막 dp[56..255]의 합
result = sum(dp[56:256]) % MOD
print(result)