# 15682번(삼차 방정식 풀기 2) 문제 : https://www.acmicpc.net/problem/15682
import sys, math
from decimal import Decimal, getcontext

input = sys.stdin.readline
getcontext().prec = 80  # 소수 11자리 계수 + 연산 여유

# 이 문제는 원래 카르다노 공식 및 판별식을 활용해서 해결할 생각이었으나
# "적어도 정수 해 1개는 갖는다"에 의해 이진 탐색으로 정수 해 하나를 찾고
# 그 다음 인수분해를 해서 2차 방정식으로 만들고
# 그리고 2차 방정식의 판별식을 통해 실수의 개수를 파악합니다.
# 혹시나 모르니 중복된 값이 존재하는지 한 번 더 확인합니다.

LBOUND = -1_000_001.0
RBOUND = 1_000_001.0
EPS_ZERO_F = 1e-12          # float용 0 판정
EPS_MERGE_D = Decimal('1e-9')  # Decimal 병합 오차
BIS_ITERS = 90

def bisect_root_float(a, b, c, d, lo, hi) :
    # f(x)=ax^3+bx^2+cx+d 이분법 (float)
    def f(x):
        return ((a*x + b)*x + c)*x + d

    flo, fhi = f(lo), f(hi)
    if abs(flo) < EPS_ZERO_F: return lo
    if abs(fhi) < EPS_ZERO_F: return hi
    # 부호가 다르다고 가정
    for _ in range(BIS_ITERS) :
        mid = (lo + hi) / 2.0
        fmid = f(mid)
        if abs(fmid) < EPS_ZERO_F :
            return mid
        if (flo > 0 and fmid < 0) or (flo < 0 and fmid > 0) :
            hi = mid
            fhi = fmid
        else :
            lo = mid
            flo = fmid
    return (lo + hi) / 2.0

def approx_real_roots_float(a, b, c, d) :
    # f'(x)로 구간을 나눠 최대 3개의 실근 근사치를 float로 찾기
    def f(x): return ((a*x + b)*x + c)*x + d
    roots = []

    m = b*b - 3.0*a*c # f'(x)=3ax^2+2bx+c 의 판별식
    if m <= EPS_ZERO_F :
        # 단조 → 1개
        roots.append(bisect_root_float(a,b,c,d, LBOUND, RBOUND))
        return roots

    s = math.sqrt(m)
    x1 = (-b - s) / (3.0*a)
    x2 = (-b + s) / (3.0*a)
    if x1 > x2: x1, x2 = x2, x1

    yL, y1, y2, yR = f(LBOUND), f(x1), f(x2), f(RBOUND)

    # [L, x1]
    if yL == 0.0     : roots.append(LBOUND)
    elif y1 == 0.0   : roots.append(x1)
    elif yL * y1 < 0 : roots.append(bisect_root_float(a,b,c,d, LBOUND, x1))
    # [x1, x2]
    if y1 * y2 < 0 : roots.append(bisect_root_float(a,b,c,d, x1, x2))
    # [x2, R]
    if y2 == 0.0     : roots.append(x2)
    elif yR == 0.0   : roots.append(RBOUND)
    elif y2 * yR < 0 : roots.append(bisect_root_float(a,b,c,d, x2, RBOUND))

    if not roots :
        # 안전장치
        roots.append(bisect_root_float(a,b,c,d, LBOUND, RBOUND))
    return roots

def solve_one(Astr, Bstr, Cstr, Dstr) :
    # (1) 입력을 Decimal로 파싱(정확)
    A = Decimal(Astr); B = Decimal(Bstr); C = Decimal(Cstr); D = Decimal(Dstr)

    # (2) 근사 실근(float)들을 구해 정수 해를 특정
    a = float(A); b = float(B); c = float(C); d = float(D)
    approx = approx_real_roots_float(a,b,c,d)

    def f_dec_at_int(k:int) -> Decimal :
        # 정수 대입은 Decimal에서 정확
        kk = Decimal(k)
        return ((A*kk + B)*kk + C)*kk + D

    int_root = None
    # 각 근사치 주변의 정수 후보들을 검사
    for r in approx :
        cand = {int(round(r)), math.floor(r), math.ceil(r)}
        for k in cand :
            if f_dec_at_int(k) == 0 :
                int_root = k
                break
        if int_root is not None:
            break

    # 정수 해가 반드시 존재(문제 보장). 혹시 못 찾았으면 더 넓게 검사(안전장치).
    if int_root is None :
        # 근사치 주변 ±3까지 훑기
        for r in approx :
            c0 = int(round(r))
            for k in range(c0-3, c0+4) :
                if f_dec_at_int(k) == 0 :
                    int_root = k
                    break
            if int_root is not None :
                break
    # 그래도 None이면(이론상 거의 불가) 전체 범위에서 희박 샘플 검사
    if int_root is None:
        for k in range(-1_000_000, 1_000_001, 49999) :
            if f_dec_at_int(k) == 0 :
                int_root = k
                break
    assert int_root is not None, "정수 해를 찾지 못했습니다(입력 보장 위반 가능)."

    # (3) (x - r)로 합성나눗셈 → A'x^2 + B'x + C'
    rD = Decimal(int_root)
    A2 = A
    B2 = B + A2 * rD
    C2 = C + B2 * rD
    # 나머지 = D + C2 * rD == 0 이어야 함
    # 2차 방정식 : A2 x^2 + B2 x + C2 = 0

    roots_dec = [rD]  # 정수 해 추가

    # (4) 2차 근의 공식 (Decimal)
    # A2 != 0 (원래 A != 0)
    Delta = B2*B2 - Decimal(4) * A2 * C2
    if Delta > 0 :
        sqrtD = Delta.sqrt()
        twoA = Decimal(2) * A2
        r2 = (-B2 - sqrtD) / twoA
        r3 = (-B2 + sqrtD) / twoA
        roots_dec.extend([r2, r3])
    elif Delta == 0 :
        r2 = (-B2) / (Decimal(2) * A2)
        roots_dec.append(r2)
    # (Delta < 0)면 실근 없음 → 정수 해만 존재

    # (5) 정렬 + 중복(중근) 병합 + -0.0 정리
    roots_dec.sort()
    merged = []
    for x in roots_dec :
        if abs(x) < Decimal('5e-13') :
            x = Decimal(0)
        if not merged or abs(x - merged[-1]) > EPS_MERGE_D :
            merged.append(x)

    # (6) 출력(오름차순). 1e-9 허용 → 10자리 고정 소수로 충분
    print(' '.join(f"{float(r):.10f}" for r in merged))

T:int = int(input().rstrip())
for _ in range(T) :
    Astr, Bstr, Cstr, Dstr = input().split()
    solve_one(Astr, Bstr, Cstr, Dstr)