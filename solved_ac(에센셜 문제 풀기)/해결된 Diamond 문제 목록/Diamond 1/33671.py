# 33671번(루미의 생일파티장 꾸미기 (EX)) : https://www.acmicpc.net/problem/33671
import math, random

MOD:int = 998244353

# 1. 64비트 정수용 Miller–Rabin 소수 판정
SMALL_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29]
def is_prime(n: int) -> bool:
    """결정적 Miller–Rabin 소수 판정 (n < 2^64 범위에서 유효)."""
    if n < 2:
        return False
    # 작은 약수들로 빠른 검사
    if n % 2 == 0:
        return n == 2
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p
    # n-1 = 2^s * d (d는 홀수)로 분해
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # 고정 밑들에 대한 Miller–Rabin 검사
    def is_composite(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return False
        return True
    # 64비트 정수에서 충분한 결정적 밑 집합
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            return True  # a가 n의 배수이면 검사 생략
        if is_composite(a):
            return False
    return True

# 2. Pollard's Rho 소인수분해
def pollard_rho(n: int) -> int:
    """Pollard's Rho 알고리즘으로 n의 비자명한 인수를 찾는다."""
    if n % 2 == 0:
        return 2
    # 임의 다항식 f(x) = x^2 + c (mod n)와 Floyd 순환 탐지 사용
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
            if d == n:
                # d = n이면 난수 다시 선택해 재시도
                break
        if 1 < d < n:
            return d

# 3. 위 도구들을 이용한 전체 소인수분해
def factorize(n: int) -> list:
    # n의 소인수들을 리스트로 반환
    if n < 2:
        return []
    if is_prime(n):
        return [n]
    factors = []
    # 2 인수 제거
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    if n == 1:
        return factors
    if is_prime(n):
        factors.append(n)
    else:
        d = pollard_rho(n)
        factors += factorize(d)
        factors += factorize(n // d)
    return factors

# 4. kMax 이하의 φ(i) 전처리 및 누적합
kMax = 2000000
phi = list(range(kMax + 1))
for p in range(2, kMax + 1):
    if phi[p] == p:  # p가 소수이면
        for j in range(p, kMax + 1, p):
            phi[j] -= phi[j] // p
Phi_prefix = [0] * (kMax + 1)
for i in range(1, kMax + 1):
    Phi_prefix[i] = Phi_prefix[i-1] + phi[i]

# 5. 메모이제이션을 이용한 Φ(n) 고속 계산
Phi_cache = {}
def Phi_summatory(n: int) -> int:
    """Φ(n) = ∑_{i=1..n} φ(i) 를 효율적으로 계산한다."""
    if n <= kMax:
        return Phi_prefix[n]
    if n in Phi_cache:
        return Phi_cache[n]
    # 공식: Φ(n) = n(n+1)//2 - ∑_{i=2..n} Φ( floor(n/i) )
    total = n * (n + 1) // 2  # 삼각수 T(n)
    i = 2
    while i <= n:
        x = n // i
        j = n // x   # floor(n/j) = x 가 유지되는 마지막 j
        total -= (j - i + 1) * Phi_summatory(x)
        i = j + 1
    Phi_cache[n] = total
    return total

# 6. L의 소인수에 대한 포함배제를 이용한 메인 계산
def compute_result(a: int, b: int) -> int:
    # b를 소인수분해 후 서로 다른 소인수만 추출
    # 정렬되지 않을 수 있으니 중복된 소인수 제거 후 정렬합니다.
    prime_factors = sorted(set(factorize(b)))
    # prime_factors 로 구성한 약수 x에 대해 Φ( floor(a/x) )를 누적
    def rec_sum(n: int, current: int, idx: int) -> int:
        if current > n:
            return 0
        # 현재 약수의 기여분 포함
        result = Phi_summatory(n // current) % MOD
        # 같은 소인수를 거듭 사용(거듭제곱)할 수 있도록 i부터 재귀
        for i in range(idx, len(prime_factors)):
            next_div = current * prime_factors[i]
            result = (result + rec_sum(n, next_div, i)) % MOD
        return result
    # x=1에서 시작하여 a에 대해 누적합 계산
    total_sum = rec_sum(a, 1, 0)
    # φ(b) = b * ∏_{p|b} (1 - 1/p) 를 곱하고 모듈러
    phi_b = b
    for p in prime_factors:
        phi_b -= phi_b // p
    result = (total_sum % MOD) * (phi_b % MOD) % MOD
    return result

# 7. 입력을 읽고 결과 출력
N, L = map(int, input().split())
print(compute_result(N, L))