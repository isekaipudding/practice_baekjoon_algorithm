# 13926번(gcd(n, k) = 1) : https://www.acmicpc.net/problem/13926
import sys
import random

input = sys.stdin.readline

# 나무위키 : https://namu.wiki/w/%EC%98%A4%EC%9D%BC%EB%9F%AC%20%ED%94%BC%20%ED%95%A8%EC%88%98
# 항목 2.1 계산 예시에 존재한 계산식을 활용합니다.

# 설마 한방에 통과하는건 아니겠지?
# 만약 통과하면 GCD(n, k) = 1(11689번)에도 제출해서 1+1 행사 챙길 것입니다.

# 큰 수 소인수분해(4149번) 문제에 제출한 소스 코드를 재활용합니다.

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

# N을 입력합니다.
N:int = int(input().rstrip())

# 이제 N을 소인수분해 합니다. 다른 점은 리스트가 아닌 집합으로 해서 중복된 소인수는 제거합니다.
S:set = set()
TEMP:int = N
while TEMP > 1 :
    divisor:int = pollardRho(TEMP)
    S.add(divisor)
    TEMP = TEMP // divisor

L:list = list(S)
L.sort()

# 오일러 피 함수를 적용하기 위해 분자와 분모를 구합니다.
numerator:int = 1 # 분자
denominator:int = 1 # 분모
for prime in L :
    numerator *= prime - 1
    denominator *= prime
    
# 오일러 피 함수를 적용하여 결과값을 출력합니다.
print(N * numerator // denominator)