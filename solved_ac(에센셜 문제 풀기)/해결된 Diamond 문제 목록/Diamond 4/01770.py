# 1770번(배수와 약수의 개수) 문제 : https://www.acmicpc.net/problem/1770
import sys
import random

input = sys.stdin.readline

# 참고 블로그 : https://hapby9921.tistory.com/entry/BOJ-1770-배수와-약수의-개수
# 코드 안 보고 기존 소스 코드를 재활용하는 방식으로 했습니다.
# (+ dp 런타임 전처리로 팩토리얼 미리 계산)

# 초기 설정
DP_LENGTH = 0
MAX = 10 ** 18

# 진짜 늘 느끼는 것인데 큰 수 소인수분해(4149번) 한 번 제대로 구현하니 날먹 가능하네ㅋㅋㅋㅋ

# 아아... 이것은 『에라토스테네스의 체』라고 한다. 소수를 쉽게 구해주지.
def sieve_of_eratosthenes(max_num) -> list :
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= max_num) :
        if (is_prime[p]) :
            for i in range(p * p, max_num + 1, p) :
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if is_prime[p]]

# 100 이하의 소수들을 미리 구합니다.
primes:list = sieve_of_eratosthenes(100)

TOTAL = 1
for p in primes :
    if TOTAL * p <= MAX :
        TOTAL *= p
        DP_LENGTH += 1

dp:list = [0 for _ in range(DP_LENGTH+1)]
# 초기값
dp[0] = 1
# 점화식
for i in range(1, DP_LENGTH+1, 1) :
    dp[i] = dp[i-1] * i

# x^y % p를 구합니다.
def power(x, y, p) -> int :
    if y < 2 :
        return x ** y % p
    else :
        z = y // 2
        if y % 2 == 0 :
            return power(x, z, p) ** 2 % p
        else :
            return x * (power(x, z, p) ** 2) % p

# 아... 이것은 『유클리드 호제법』이라는 것이다.
def gcd(a, b) -> int :
    while b :
        a, b = b, a % b
    return a

# 밀러-라빈 소수 판별법 알고리즘(이럴 수가! 더 큰 소수를 판별해준다고!?)
def miller_rabin(n, a) -> bool :
    r:int = 0
    d:int = n - 1
    while d % 2 == 0 :
        r += 1
        d = d // 2

    x:int = power(a, d, n)
    if x == 1 or x == n - 1 :
        return True

    for _ in range(r - 1) :
        x = power(x, 2, n)
        if x == n - 1 :
            return True
    return False

# 소수 판정 알고리즘
def is_prime(n) -> bool :
    if n == 1 :
        return False
    if n == 2 or n == 3 :
        return True
    if n % 2 == 0 :
        return False
    for a in primes :
        if n == a :
            return True
        if not miller_rabin(n, a) :
            return False
    return True

# 폴라드 로 알고리즘(무작위로 해도 소인수가 나온다고!?)
def pollardRho(n) -> int :
    if is_prime(n) :
        return n
    if n == 1 :
        return 1
    if n % 2 == 0 :
        return 2
    x:int = random.randrange(2, n)
    y:int = x
    c:int = random.randrange(1, n)
    d:int = 1
    while d == 1 :
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n :
            return pollardRho(n)
    if is_prime(d) :
        return d
    else :
        return pollardRho(d)
    
T:int = int(input().rstrip())

for _ in range(T) :
    # N을 입력합니다.
    N:int = int(input().rstrip())
    
    # 예외 처리
    if N == 1 :
        print(1)
        continue
    if N == 4 :
        print(1)
        continue

    # 이제 N을 소인수분해 합니다.
    L:list = []
    while N > 1 :
        divisor:int = pollardRho(N)
        L.append(divisor)
        N = N // divisor

    # 정렬합니다.
    L.sort()
    
    S:set = set()
    D:dict = dict() # key:value = 밑:지수
    
    for p in L :
        if p not in S :
            S.add(p)
            D[p] = 1
        else :
            D[p] += 1
            
    exponent:list = max(list(D.values()))

    if exponent > 1 :
        print(-1)
        continue
    if exponent == 1 :
        index:int = len(list(D.keys()))
        print(dp[index])
        continue
    
    raise ValueError("N은 자연수가 아니므로 소인수분해가 불가능합니다.")