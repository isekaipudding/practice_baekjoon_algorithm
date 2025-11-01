# -*- coding: utf-8 -*-
# EV[p][q] exact builder (Fraction DP)
# - 유효한 경우: p <= q, (q - p) % 6 == 0
# - 점화식 (S_excl 사용):
#   EV[p,q] = (2/3) * [ sum_{i=0..p-1} C(p,i) * ( sum_{j≡i(6), 0<=j<=q} C(q,j)*EV[i,j] )
#                       + sum_{j≡p(6), 0<=j<q} C(q,j)*EV[p,j] ]
#              / ( 2^(p+q) - 1 )
#
#  * 대칭성 EV[p,q] = EV[q,p] 를 사용하여 읽기만 대칭 접근합니다(쓰기 인덱스는 항상 p<=q).
#  * MAXN까지 정확 분수(기약분수)로 계산합니다.

# 연구 자료이며 정확한 값(기약분수)이 출력되니 뒤를 부탁합니다.
# MAXN은 최소 400 정도 해야 합니다.

from fractions import Fraction
from math import comb
from decimal import Decimal, getcontext
import sys
import time

# 타이머 시작
start = time.time()

def is_valid_pair(p: int, q: int) -> bool:
    return p <= q and (q - p) % 6 == 0

def build_ev_exact(MAXN: int):
    EV = [[None] * (MAXN + 1) for _ in range(MAXN + 1)]
    EV[0][0] = Fraction(1, 1)

    # 2의 거듭제곱 미리 계산
    pow2 = [1] * (2 * MAXN + 1)
    for s in range(1, 2 * MAXN + 1):
        pow2[s] = pow2[s - 1] * 2

    # 대각선(s = p+q) 순회
    for s in range(0, 2 * MAXN + 1):
        print(f"process = {100 * s / (2 * MAXN)}%")
        for q in range(0, MAXN + 1):
            p = s - q
            if p < 0 or p > MAXN:
                continue
            if not is_valid_pair(p, q):
                continue
            if p == 0 and q == 0:
                continue

            total = Fraction(0, 1)

            # (1) i < p 부분: sum_i C(p,i) * [ sum_{j≡i(6)} C(q,j)*EV[i,j] ]
            for i in range(0, p):
                start = i % 6
                tsum = Fraction(0, 1)
                for j in range(start, q + 1, 6):
                    # 읽을 때만 대칭 활용
                    vij = EV[i][j] if i <= j else EV[j][i]
                    if vij is None:
                        continue
                    tsum += Fraction(comb(q, j), 1) * vij
                if tsum:
                    total += Fraction(comb(p, i), 1) * tsum

            # (2) 같은 행(p)에서 j < q, j≡p(6): sum_{j<q} C(q,j)*EV[p,j]
            start = p % 6
            for j in range(start, q, 6):
                vij = EV[p][j] if p <= j else EV[j][p]
                if vij is None:
                    continue
                total += Fraction(comb(q, j), 1) * vij

            # (3) 최종 대입
            EV[p][q] = Fraction(2, 3) * total / (pow2[p + q] - 1)

    return EV

if __name__ == "__main__":
    MAXN = 60
    EV = build_ev_exact(MAXN)

    # EV[60][60] 결과 (분자, 분모) 출력
    v = EV[MAXN][MAXN]
    num, den = v.numerator, v.denominator
    print(f"EV[{MAXN}][{MAXN}] =", (num, den))

    # Decimal로 원하는 자리수 출력(예: 100자리)
    getcontext().prec = 120  # 내부 정밀도(충분히 크게)
    dec_digits = 100         # 소수점 이하 자리수
    val = (Decimal(num) / Decimal(den))
    # 고정 소수점 포맷
    print(f"EV[{MAXN}][{MAXN}] (Decimal, {dec_digits} digits) = {format(val, f'.{dec_digits}f')}")
    
    # 타이머 종료 및 출력
    end = time.time()
    print(f"Elapsed time: {end - start:.3f} sec", file=sys.stderr)