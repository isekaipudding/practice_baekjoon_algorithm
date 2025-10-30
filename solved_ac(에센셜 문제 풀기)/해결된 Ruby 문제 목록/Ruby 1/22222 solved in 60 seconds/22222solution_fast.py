# solution_fast.py
# BOJ 22222 지애 상수 — EV 희소 테이블 재사용 + 고속 합산 최적화

# 실제 ev_sparse.py는 알집 파일로 공유합니다.
# 실제로 22222.py의 일부 소스 코드를 수정하여 ev_sparse_sample.py 형식대로 해서
# (p-q) % 6 == 0인 데이터들을 사전 형식으로 저장하도록 변경하면 됩니다.
# 그러면 실제 ev_sparse.py를 얻을 수 있습니다.

from decimal import Decimal, getcontext, ROUND_HALF_UP
from ev_sparse_sample import EV_SPARSE  # p<=q, (p-q)%6==0만 포함된 희소 테이블
import sys
import time

# 실제 ev_sparse.py로 테스트 해본 결과 약 4초가 나왔습니다. 엄청난 성과입니다.
# 백준의 512kB 제한만 아니었다면 이 소스 코드는 AC 판정 받았을 것입니다.

# 타이머 시작
start = time.time()

# ---------------------------------------
# 설정
# ---------------------------------------
PRINT_DIGITS = 222
N_TERMS = 1000         # 테일러 항 (권장: 1000)
MARGIN = 80            # 정밀 여유
getcontext().prec = PRINT_DIGITS + MARGIN

# ---------------------------------------
# sqrt(1+z) 테일러 계수: c[n] = binom(1/2, n)
# c[0]=1,  c[n] = c[n-1] * ((3/2 - n) / n)
# ---------------------------------------
def build_sqrt_coeff(nmax: int):
    c = [Decimal(0)] * (nmax + 1)
    c[0] = Decimal(1)
    three_half = Decimal(3) / Decimal(2)
    for n in range(1, nmax + 1):
        c[n] = c[n - 1] * (three_half - Decimal(n)) / Decimal(n)
    return c

# ---------------------------------------
# 복소수 거듭제곱 표: U^n = a[n] + i b[n]
# ---------------------------------------
def build_complex_powers(ur: Decimal, ui: Decimal, nmax: int):
    a = [Decimal(0)] * (nmax + 1)
    b = [Decimal(0)] * (nmax + 1)
    a[0] = Decimal(1)
    b[0] = Decimal(0)
    for n in range(1, nmax + 1):
        ar = a[n - 1] * ur - b[n - 1] * ui
        ai = a[n - 1] * ui + b[n - 1] * ur
        a[n], b[n] = ar, ai
    return a, b

# ---------------------------------------
# 희소 EV를 (p=q)와 (p<q)로 분리하여 평탄화 (1회)
# diag_pairs: list[(p, ev_pp)]
# offP/offQ/offEV: 나란히 인덱싱되는 평행 리스트
# ---------------------------------------
def build_pairs_split(ev_sparse, nmax):
    diag_pairs = []                 # (p, ev_pp)
    offP, offQ, offEV = [], [], []  # 평행 리스트
    for p, row in ev_sparse.items():
        if p > nmax:
            continue
        # 대각 p==q
        ev_pp = row.get(p)
        if ev_pp is not None:
            diag_pairs.append((p, ev_pp))
        # 오프대각 p<q
        for q, ev in row.items():
            if q <= p or q > nmax:
                continue
            offP.append(p); offQ.append(q); offEV.append(ev)
    return diag_pairs, offP, offQ, offEV

DIAG_PAIRS, OFFP, OFFQ, OFFEV = build_pairs_split(EV_SPARSE, N_TERMS)
TWICE = Decimal(2)  # 상수 캐시

# ---------------------------------------
# 고속 합산:
# E[ sqrt((1 + U D)(1 + U* D*)) ]
#  = sum_{p}   (alpha[p]^2 + beta[p]^2) * EV[p][p]
#   + 2*sum_{p<q} (alpha[p]*alpha[q] + beta[p]*beta[q]) * EV[p][q]
# where alpha[n] = a[n]*c[n], beta[n] = b[n]*c[n]
# ---------------------------------------
def E_abs_1_plus_UD_fast(ur: Decimal, ui: Decimal, c):
    a, b = build_complex_powers(ur, ui, N_TERMS)
    alpha = [a[i] * c[i] for i in range(N_TERMS + 1)]
    beta  = [b[i] * c[i] for i in range(N_TERMS + 1)]

    total = Decimal(0)
    # 대각
    for p, evpp in DIAG_PAIRS:
        ap = alpha[p]; bp = beta[p]
        total += (ap * ap + bp * bp) * evpp
    # 오프대각 (배수 2)
    offP = OFFP; offQ = OFFQ; offEV = OFFEV
    for i in range(len(offP)):
        p = offP[i]; q = offQ[i]; ev = offEV[i]
        total += (alpha[p] * alpha[q] + beta[p] * beta[q]) * ev * TWICE
    return total

# ---------------------------------------
# 메인: 안정화 전개 + 자기유사 보정
# - X=1/2, a=1/4, x ∈ {0 (1/3), 1 (1/9), w (2/9), w^2 (2/9)}  ← conj 쌍 통합
# - U_eval = X + x*X^2,  U' = a / U_eval
# - 케이스 기여 = |U_eval| * E_abs_1_plus_UD_fast(U')
# - E|D| = (72/85) * Σ p(x) * 케이스 기여
# ---------------------------------------
def main():
    c = build_sqrt_coeff(N_TERMS)

    X = Decimal(1) / Decimal(2)
    X2 = X * X
    a_quarter = Decimal(1) / Decimal(4)

    sqrt3 = Decimal(3).sqrt()
    wr = Decimal(1) / Decimal(2)
    wi = sqrt3 / Decimal(2)

    # w^k
    wk = [(Decimal(1), Decimal(0))]
    for _ in range(5):
        pr = wk[-1][0] * wr - wk[-1][1] * wi
        pi = wk[-1][0] * wi + wk[-1][1] * wr
        wk.append((pr, pi))

    # conj 쌍을 합쳐 4케이스로 축소
    cases = [
        (Decimal(0), Decimal(0), Decimal(1) / Decimal(3)),   # x=0
        (wk[0][0], wk[0][1], Decimal(1) / Decimal(9)),       # x=1
        (wk[1][0], wk[1][1], Decimal(2) / Decimal(9)),       # x=w
        (wk[2][0], wk[2][1], Decimal(2) / Decimal(9)),       # x=w^2
    ]

    total = Decimal(0)
    for xr, xi, prob in cases:
        # U_eval = X + x*X^2
        Uer = X + xr * X2
        Uei = xi * X2
        # |U_eval| and U' = a / U_eval
        abs2 = Uer * Uer + Uei * Uei
        Uabs = abs2.sqrt()
        Ur = (a_quarter * Uer) / abs2
        Ui = (-a_quarter * Uei) / abs2
        # 고속 합산
        part = Uabs * E_abs_1_plus_UD_fast(Ur, Ui, c)
        total += prob * part

    result = total * Decimal(72) / Decimal(85)
    q = result.quantize(Decimal('1e-222'), rounding=ROUND_HALF_UP)
    print(f"{q:.{PRINT_DIGITS}f}")

if __name__ == "__main__":
    main()
    # 타이머 종료 및 출력
    end = time.time()
    print(f"Elapsed time: {end - start:.3f} sec", file=sys.stderr)