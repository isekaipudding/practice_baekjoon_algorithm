# fixedpoint_jiae_22222.py
# -*- coding: utf-8 -*-
# BOJ 22222 지애 상수 — 정수 고정소수점 버전(반올림 일관화)
# - 핵심: 버림(//) → 반올림(half-up)으로 일관 교체
# - SCALE=10**300 으로 스케일을 크게 잡아 미세 손실 최소화
# - N_MAX는 1000

import sys
import math
import decimal
import time

# GPT 5.1 Thinking mode + Gemini 3.0 Thinking mode 둘 다 혼합하여 사용했습니다.
# 아주 수많은 시도 끝에 이것이 만약 AC 판정 받으면 드디어!!!!!! 성공입니다!!!

# 일부 파이썬 버전에서 안전장치
try:
    sys.set_int_max_str_digits(1_000_000)
except Exception:
    pass

# -----------------------------
# 0) 공용 유틸 (정수 반올림)
# -----------------------------
def div_round(num: int, den: int) -> int:
    """Half-up rounding for integer division."""
    if den == 0:
        raise ZeroDivisionError
    if num >= 0:
        return (num + den // 2) // den
    else:
        return -(((-num) + den // 2) // den)

def mul_div_round(a: int, b: int, den: int) -> int:
    """Half-up rounding for (a*b)/den."""
    return div_round(a * b, den)

def isqrt_round(n: int) -> int:
    """반올림 정수 제곱근."""
    y = math.isqrt(n)
    lo = y * y
    hi = (y + 1) * (y + 1)
    # 더 가까운 쪽으로 반올림
    if n - lo > hi - n:
        return y + 1
    else:
        return y

# ---------------------------------------
# 1) 설정 파라미터
# ---------------------------------------
N_MAX = 1000                # 테일러 최대 차수
OUTPUT_DIGITS = 222        # 최종 출력 소수 자리수
SCALE_EXP = 300            # 고정소수점 스케일 지수
SCALE = 10 ** SCALE_EXP    # 고정소수점 스케일(크게! 오차 억제)
# (참고) 계산 시간/메모리는 N_MAX^3-ish 경향. 너무 키우면 매우 무거워집니다.

# ---------------------------------------
# 2) 전처리: 이항계수 / (2^(s) - 1)
# ---------------------------------------
def build_comb(nmax: int):
    COMB = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    for i in range(nmax + 1):
        COMB[i][0] = 1
        for j in range(1, i + 1):
            COMB[i][j] = COMB[i - 1][j - 1] + COMB[i - 1][j]
    return COMB

def build_pow2_sub1(nmax: int):
    POW2_SUB_1 = [0] * (2 * nmax + 1)
    cur = 1
    for s in range(1, 2 * nmax + 1):
        cur <<= 1  # 2^s
        POW2_SUB_1[s] = cur - 1
    return POW2_SUB_1

# ---------------------------------------
# 3) EV 테이블(스케일= SCALE) + RowTrans 캐시
# ---------------------------------------
def build_EV_fixed(N_MAX: int, COMB, POW2_SUB_1):
    # EV[p][q]는 p<=q, (q-p)%6==0 만 사용. 저장은 스케일된 정수.
    EV = [[0] * (N_MAX + 1) for _ in range(N_MAX + 1)]
    EV[0][0] = SCALE

    # RowTrans[i][rem][k] = sum_{j≡rem(mod 6), j<=k} C(k,j)*EV[i][j]
    RowTrans = [[[0] * (N_MAX + 1) for _ in range(6)] for _ in range(N_MAX + 1)]

    # i=0 초기화
    v00 = EV[0][0]
    for k in range(N_MAX + 1):
        RowTrans[0][0][k] = v00  # C(k,0)*EV[0][0] = 1*v00

    # 대각선(s=p+q) 루프 (짝수 s만 유효)
    for s in range(2, 2 * N_MAX + 1, 2):
        start_p = max(0, s - N_MAX)
        end_p = s // 2

        # (q-p) % 6 == 0 조건을 만족하는 p부터 시작(= s - 2p ≡ 0 (mod 6))
        rem_s = s % 6
        while start_p <= end_p:
            if (2 * start_p) % 6 == rem_s:
                break
            start_p += 1
        if start_p > end_p:
            continue

        for p in range(start_p, end_p + 1, 3):  # 2p ≡ s (mod 6) → p를 mod 3 간격으로 순회
            q = s - p

            # Sum A: sum_{i=0..p-1} C(p,i) * ( sum_{j≡i(6)} C(q,j) * EV[i][j] )
            sum_A = 0
            for i in range(p):
                bucket = RowTrans[i][i % 6]
                val = bucket[q]  # sum_{j≡i(6), j<=q} C(q,j)*EV[i][j]
                if val:
                    sum_A += COMB[p][i] * val

            # Sum B: sum_{j≡p(6), 0<=j<q} C(q,j)*EV[p][j]
            sum_B = 0
            rem_p = p % 6
            for j in range(rem_p, q, 6):
                val = EV[p][j] if p <= j else EV[j][p]
                if val:
                    sum_B += COMB[q][j] * val

            total_sum = sum_A + sum_B
            # EV[p][q] = (2/3) * total_sum / (2^(p+q)-1)
            # 스케일된 EV가 필요 → (2*total_sum) / (3*(2^s-1))  [여기서 total_sum 자체가 스케일 포함]
            ev_val = div_round(2 * total_sum, 3 * POW2_SUB_1[s])
            EV[p][q] = ev_val

            if ev_val == 0:
                continue

            # RowTrans 업데이트: 새로 들어온 (p,q) 반영
            rem_q = q % 6
            target_row = RowTrans[p][rem_q]
            for k in range(q, N_MAX + 1):
                target_row[k] += COMB[k][q] * ev_val

            if p != q:
                rem_p_val = p % 6
                target_row_sym = RowTrans[q][rem_p_val]
                for k in range(p, N_MAX + 1):
                    target_row_sym[k] += COMB[k][p] * ev_val

    return EV

# ---------------------------------------
# 4) sqrt(1+z) 계수 c[n] (스케일 = SCALE)
#    c[0]=1, c[n] = c[n-1]*((3/2 - n)/n)
# ---------------------------------------
def build_sqrt_coeff_scaled(N_MAX: int):
    c = [0] * (N_MAX + 1)
    c[0] = SCALE
    for n in range(1, N_MAX + 1):
        prev = c[n - 1]
        # c[n] = prev * (3/2 - n) / n
        #      = prev * (1.5 - n) / n = prev * (3 - 2n) / (2n)
        num = prev * (3 - 2 * n)
        den = 2 * n
        c[n] = div_round(num, den)
    return c

# ---------------------------------------
# 5) 복소수 연산(스케일 = SCALE)
# ---------------------------------------
def complex_mul_scaled(r1, i1, r2, i2):
    # (r1+i i1)*(r2+i i2) / SCALE  (half-up)
    nr = mul_div_round(r1, r2, SCALE) - mul_div_round(i1, i2, SCALE)
    ni = mul_div_round(r1, i2, SCALE) + mul_div_round(i1, r2, SCALE)
    return nr, ni

# ---------------------------------------
# 6) 메인 계산
# ---------------------------------------
def solve():
    # 이항계수, 2^s-1
    COMB = build_comb(N_MAX)
    POW2_SUB_1 = build_pow2_sub1(N_MAX)

    # EV 빌드(정확 정수 스케일)
    EV = build_EV_fixed(N_MAX, COMB, POW2_SUB_1)

    # 비어 있지 않은 항만 뽑아 sparse로 이용
    ev_items = []
    for p in range(N_MAX + 1):
        for q in range(p, N_MAX + 1):
            val = EV[p][q]
            if val != 0:
                ev_items.append((p, q, val))

    # sqrt(1+z) 계수
    COEFF_SQRT = build_sqrt_coeff_scaled(N_MAX)

    # √3 정수 반올림
    decimal.getcontext().prec = 360
    SQRT3_INT = int((decimal.Decimal(3).sqrt() * decimal.Decimal(SCALE)).to_integral_value(rounding=decimal.ROUND_HALF_UP))

    HALF = SCALE // 2
    QUARTER = SCALE // 4

    # w = exp(i*pi/3) = 1/2 + i*sqrt(3)/2 (스케일 반올림)
    UR_BASE = HALF
    UI_BASE = div_round(SQRT3_INT, 2)

    # w^k (k=0,1,2만 필요) — 스케일 유지
    wk = [(SCALE, 0)]
    cur_r, cur_i = SCALE, 0
    for _ in range(2):
        nr, ni = complex_mul_scaled(cur_r, cur_i, UR_BASE, UI_BASE)
        wk.append((nr, ni))
        cur_r, cur_i = nr, ni

    # 케이스: x=0,1,w,w^2  (확률 1/3, 1/9, 2/9, 2/9)
    CASES = [
        (0, 0, 1, 3),
        (wk[0][0], wk[0][1], 1, 9),
        (wk[1][0], wk[1][1], 2, 9),
        (wk[2][0], wk[2][1], 2, 9),
    ]

    final_total = 0

    for xr, xi, prob_n, prob_d in CASES:
        # U_eval = X + x*X^2, X=1/2, X^2=1/4
        Uer = HALF + mul_div_round(xr, QUARTER, SCALE)
        Uei = mul_div_round(xi, QUARTER, SCALE)

        # |U| = sqrt(Uer^2 + Uei^2)  (스케일 유지)
        A = Uer * Uer + Uei * Uei       # scale^2
        abs_val = isqrt_round(A)        # |U| * SCALE

        # U' = a / U_eval,  a=1/4
        # Re(U')*SCALE = round((QUARTER * Uer * SCALE) / A)
        # Im(U')*SCALE = round((-QUARTER * Uei * SCALE) / A)
        if A == 0:
            Ur = 0
            Ui = 0
        else:
            Ur = div_round(QUARTER * Uer * SCALE, A)
            Ui = -div_round(QUARTER * Uei * SCALE, A)

        # (Ur+iUi)^n * c[n]  → alpha[n], beta[n] (각각 스케일=SCALE)
        alpha = [0] * (N_MAX + 1)
        beta = [0] * (N_MAX + 1)
        cr, ci = SCALE, 0  # (Ur+iUi)^0

        for n in range(N_MAX + 1):
            alpha[n] = mul_div_round(cr, COEFF_SQRT[n], SCALE)
            beta[n]  = mul_div_round(ci, COEFF_SQRT[n], SCALE)
            cr, ci = complex_mul_scaled(cr, ci, Ur, Ui)

        # Σ_{p} (α_p^2+β_p^2)EV[p,p] + 2 Σ_{p<q} (α_pα_q+β_pβ_q)EV[p,q]
        term_sum = 0
        for p, q, val in ev_items:
            dot = mul_div_round(alpha[p], alpha[q], SCALE) + mul_div_round(beta[p], beta[q], SCALE)
            if p == q:
                term_sum += mul_div_round(dot, val, SCALE)
            else:
                term_sum += mul_div_round(dot * 2, val, SCALE)

        part = mul_div_round(abs_val, term_sum, SCALE)
        final_total += div_round(part * prob_n, prob_d)

    # 최종 스케일 결과: (72/85) * total
    result = div_round(final_total * 72, 85)  # result는 SCALE=10^300 배 스케일의 정수

    # -----------------------------
    # 출력(소수점 222자리, half-up 반올림)
    # -----------------------------
    # result / 10^300 을 222자리로 반올림 출력: 즉, 10^(300-222) 자리에서 반올림
    shift = SCALE_EXP - OUTPUT_DIGITS
    cut = 10 ** shift
    last_digit = (result // (cut // 10)) % 10
    final_int  = result // cut
    if last_digit >= 5:
        final_int += 1

    # 반드시 222자리 0-패딩으로 출력
    print(f"0.{final_int:0{OUTPUT_DIGITS}d}")

if __name__ == "__main__":
    # 타이머 시작
    start = time.time()
    solve()
    # 타이머 종료 및 출력
    end = time.time()
    print(f"Elapsed time: {end - start:.3f} sec", file=sys.stderr)