# 19329번(GCD) : https://www.acmicpc.net/problem/19329
import sys
import random

input = sys.stdin.readline

# 아아... 이것은 『유클리드 호제법』라고 한다.
def gcd(a: int, b: int) -> int :
    while b :
        a, b = b, a % b
    return abs(a)

# (x * y) % mod 연산
def mul_mod(x: int, y: int, mod: int) -> int :
    return (x * y) % mod

# 64비트 정수에 대한 결정적 Miller–Rabin 소수 판별
def is_prime(n: int) -> bool :
    if n < 2 :
        return False
    # 작은 소수들로 먼저 검사
    small_bases:list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_bases :
        if n % p == 0 :
            return n == p
    # n-1 = d * 2^s 꼴로 변환
    d, s = n - 1, 0
    while not (d & 1) :
        d >>= 1
        s += 1
    # 테스트 베이스
    test_bases:tuple = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for a in test_bases :
        if a % n == 0 :
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1 :
            continue
        for _ in range(s - 1) :
            x = mul_mod(x, x, n)
            if x == n - 1 :
                break
        else:
            return False
    return True

# Pollard's Rho 알고리즘을 이용한 비소수 분할 함수
def pollard_rho(n: int) -> int :
    if n % 2 == 0 :
        return 2
    if is_prime(n) :
        return n
    while True :
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        # x, y를 tortoise-hare 방식으로 업데이트
        while d == 1 :
            x = (mul_mod(x, x, n) + c) % n
            y = (mul_mod(y, y, n) + c) % n
            y = (mul_mod(y, y, n) + c) % n
            d = gcd(x - y, n)
        if d != n:
            return d

# 재귀적으로 n을 소인수분해하여 prime 리스트(out)에 추가
def factorize(n: int, out: list) -> None :
    if n == 1 :
        return
    if n % 2 == 0 :
        out.append(2)
        factorize(n // 2, out)
    elif is_prime(n):
        out.append(n)
    else:
        d:int = pollard_rho(n)
        factorize(d, out)
        factorize(n // d, out)

# 소인수 리스트를 (소수, 지수) 튜플 리스트로 압축
def compress(primes: list) -> list :
    count_map = {}
    for p in primes :
        count_map[p] = count_map.get(p, 0) + 1
    return list(count_map.items())

# SOS DP: 특정 prime^exp에 대해 DFS 방식으로 값 전파
def process_dfs(count: dict,
                prime_list: list,
                target_prime: tuple,
                total_primes: int,
                index: int,
                value: int) -> None :
    p0, e0 = target_prime
    # 모든 prime들을 처리했다면 실제 전파 실행
    if index == total_primes:
        TEMP = value * pow(p0, e0, 10**18)  # 임의로 큰 mod 사용
        for _ in range(e0, 0, -1) :
            key = TEMP // p0
            freq = count.get(TEMP, 0)
            count[key] = count.get(key, 0) + freq
            TEMP //= p0
    else:
        p, e = prime_list[index]
        if p == p0 :
            process_dfs(count, prime_list, target_prime,
                        total_primes, index + 1, value)
        else:
            TEMP = value
            for _ in range(e + 1) :
                process_dfs(count, prime_list, target_prime,
                            total_primes, index + 1, TEMP)
                TEMP *= p

N, K = map(int, input().split())
L:list = list(map(int, input().split()))

result:int = 0
pivots:int = min(N, 20)
visited:list = [False for _ in range(N)]

# 20번 이내 랜덤 피벗 시도
for _ in range(pivots) :
    index:int = random.randrange(N)
    while visited[index] :
        index = random.randrange(N)
    visited[index] = True

    # 1) 모든 원소와 피벗의 gcd 빈도 계산
    count:set = {}
    pivot:int = L[index]
    for v in L :
        g = gcd(v, pivot)
        count[g] = count.get(g, 0) + 1

    # 2) 피벗 소인수분해 및 압축
    facs = []
    factorize(pivot, facs)
    primes = compress(facs)
    size = len(primes)

    # 3) SOS DP를 DFS로 전파
    for prime in primes :
        process_dfs(count, primes, prime, size, 0, 1)

    # 4) 필요한 빈도(n-K) 이상인 최대 d 찾기
    need = N - K
    for d, c in count.items() :
        if c >= need and d > result :
            result = d

print(result)