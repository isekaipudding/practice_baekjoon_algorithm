# 14854번(이항 계수 6) : https://www.acmicpc.net/problem/14854
from typing import List, Tuple
import sys

input = sys.stdin.readline

# 공부를 위해 참고 자료를 정리하는데 GPT의 도움을 받았습니다.
# 유용한 자료들이 많이 존재하니 구경 한 번 해보세요.
# 게시판에 있던 테스트 케이스로 실험해본 결과 모두 통과되었습니다. 과연 실제 결과는 TLE? AC?

# 참고 자료(개념/정리)
# - Lucas's theorem (루카스 정리, 소수 p 법에서 자리수별 조합 분해)
#   https://en.wikipedia.org/wiki/Lucas%27s_theorem
# - Chinese Remainder Theorem (CRT, 서로소 법끼리 결합)
#   https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# - Legendre's formula (레장드르 공식, ν_p(n!) = Σ floor(n/p^i))
#   https://en.wikipedia.org/wiki/Legendre%27s_formula
# - Kummer's theorem (쿠머 정리, ν_p(C(n,k)) carries 해석)
#   https://en.wikipedia.org/wiki/Kummer%27s_theorem
# - Hensel's lemma (헨셀 보정/리프팅 아이디어; 단위 원소 역원 올리기 관점 연결)
#   https://en.wikipedia.org/wiki/Hensel%27s_lemma

# 참고 자료(프라임 거듭제곱 법에서 C(n,k) 계산)
# - Andrew Granville, "Binomial Coefficients modulo prime powers"
#   HTML : https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/binomial.html
#   논문 목록 : https://dms.umontreal.ca/~andrew/Web.Publications1.pdf
# - 구현 아이디어 요약(팩토리얼의 p-지수와 p-free 부분 분해) :
#   Codeforces 블로그(개념 정리): https://codeforces.com/blog/entry/116681

# 비고
# - 본 구현은 n! = p^t * a (gcd(a,p)=1)로 분해하여 t와 a(mod p^k)를 구한 뒤
#   C(n,k) = p^{t_n - t_k - t_{n-k}} * (a_n * (a_k a_{n-k})^{-1}) (mod p^k)
#   를 계산하고, (27,11,13,37) 결과를 CRT로 결합합니다.

# 타입 정의 (C++의 using/typedef 느낌적인 느낌)
CTX = Tuple[int, int, int, List[int], List[int], List[Tuple[int, int]], int]
P_INDEX, K_INDEX, MOD_INDEX, INV_INDEX, F_INDEX, FF_INDEX, MX_INDEX = range(7)

# 큰 수 소인수분해(4149번)에서 미리 계산하여 튜플로 저장합니다.
MOD_ALL:int = 142857  # 3^3 * 11 * 13 * 37
FACTORS:List[Tuple[int, int]] = [(3, 3), (11, 1), (13, 1), (37, 1)]

# 공용 유틸
def egcd(a: int, b: int) -> Tuple[int, int, int] :
    if b == 0 :
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)

# 모듈러 역원
def inv_mod(a: int, m: int) -> int :
    g, x, _ = egcd(a % m, m)
    # 반례를 잡기 위한 ValueError 예외 호출
    if g != 1 :
        raise ValueError("inverse does not exist")
    return x % m

# 중국인의 나머지 정리 CRT
# CRT는 FFT와 관련된 NTT에서도 사용됩니다.
def crt(res: List[int], mods: List[int]) -> int :
    # x ≡ res[i] (mod mods[i]) (서로소) 결합
    x = 0
    mprod = 1
    for r, m in zip(res, mods):
        t = ((r - x) % m) * inv_mod(mprod % m, m) % m
        x += mprod * t
        mprod *= m
    return x % mprod

# p^k용 전처리/컨텍스트
def build_CTX(p: int, k: int) -> CTX :
    mod = p ** k
    # mod가 작아도 빠른 fct를 위해 5만까지 누적 테이블 준비
    mx = max(mod, 50_000)

    # inv_p: modulo p에서의 역원(1..p-1)
    inv_p: List[int] = [0] * p
    for i in range(1, p):
        inv_p[i] = pow(i, p - 2, p)

    # F[i]  : 1..i의 p-배수 제거(p-free) 곱 (mod p^k)
    # Ff[i] : (nu_p(i!), p-free(i!) mod p^k)
    F: List[int] = [1]
    Ff: List[Tuple[int, int]] = [(0, 1)]

    curF = 1
    curVp, curUnit = 0, 1
    for i in range(1, mx) :
        if i % p != 0:
            curF = (curF * i) % mod
        F.append(curF)

        ti = i
        tk = 0
        while ti % p == 0:
            ti //= p
            tk += 1
        curVp += tk
        curUnit = (curUnit * ti) % mod
        Ff.append((curVp, curUnit))

    return (p, k, mod, inv_p, F, Ff, mx)

# p^k에서의 역원(단위 원소만) : 뉴턴 보정
def fast_inv_unit(z: int, CTX: CTX) -> int :
    p, _, mod, inv_p, *_ = CTX
    # 반례를 잡기 위한 ZeroDivisionError 예외 호출
    if z % p == 0 :
        raise ZeroDivisionError("trying to invert a multiple of p")
    r = inv_p[z % p]  # mod p에서 시작
    while (r * z) % mod != 1:
        r = (r * (2 - (r * z) % mod)) % mod  # lift to mod p^k
    return r

# n! = p^vp * unit (mod p^k)
def fct(n: int, CTX: CTX) -> Tuple[int, int] :
    p, _, mod, _, F, Ff, mx = CTX
    vp = 0
    unit = 1

    # 큰 n은 블록(길이 mod) 단위 처리: p-free 곱의 주기성 활용 (odd p : 블록 곱 = -1)
    while n >= mx :
        t = n // p
        b = n // mod
        vp += t
        unit = (unit * F[n - b * mod]) % mod # 나머지 구간
        if b & 1 : # odd block count -> 곱에 -1
            unit = (-unit) % mod
        n = t

    add_vp, add_unit = Ff[n]
    vp += add_vp
    unit = (unit * add_unit) % mod
    return vp, unit

# C(n, r) mod p^k
def nCr_mod_pk(n: int, r: int, CTX: CTX) -> int :
    if r < 0 or r > n :
        return 0
    p, k, mod, *_ = CTX
    vp_n, a_n = fct(n, CTX)
    vp_r, a_r = fct(r, CTX)
    vp_nr, a_nr = fct(n - r, CTX)

    vp = vp_n - vp_r - vp_nr
    if vp >= k :
        return 0 # p^k가 나눔
    denom = (a_r * a_nr) % mod
    inv_d = fast_inv_unit(denom, CTX)
    return (pow(p, vp, mod) * a_n % mod) * inv_d % mod

T:int = int(input().strip())
CTXs:List[CTX] = [build_CTX(p, k) for p, k in FACTORS]
mods:List[int] = [p ** k for p, k in FACTORS]

for _ in range(T) :
    n, r = map(int, input().split())
    residues = [nCr_mod_pk(n, r, CTX) for CTX in CTXs]
    result:int = crt(residues, mods)  # modulo 142857
    print(result)