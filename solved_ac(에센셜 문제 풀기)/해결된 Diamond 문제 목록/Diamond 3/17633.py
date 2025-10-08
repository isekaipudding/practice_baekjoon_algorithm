# 17633번(제곱수의 합 (More Huge)) : https://www.acmicpc.net/problem/17633
import sys
import random
import math
from collections import Counter

input = sys.stdin.readline

# N이 최대 10^18이므로 큰 수 소인수분해(4149번)에 제출했던 소스 코드를 재활용합니다.
# 어제 자기 전에 Four Squares를 어떻게 풀까 하다가 아래에 있는 3가지 공식을 응용하면 되는 것으로 판단했습니다.
# 추가로 어제 해결했던 GCD(19329번) 풀고 난 뒤 영감을 얻었습니다.
# "아! 이거 제곱수의 합 문제에서 큰 수 소인수분해를 적용하면 more huge도 가능하겠다!"
# 그래서 어제 떠올린 영감을 바탕으로 이 문제를 도전합니다.
# 이거 성공하면 무려 루비4인 제곱수의 합 2 (more huge)도 도전할 것입니다. 불가능이란 없습니다.

# 라그랑주의 네 제곱수 정리 : https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
# 르장드르의 세 제곱수 정리 : https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
# 페르마의 두 제곱수 정리 : https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares

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
    
# 제곱수의 합(1699번)에 제출했던 소스 코드를 재활용합니다.
def lagrange(N) :
    # 완전 거듭제곱인 경우 어떠한 법칙 적용하지 않고 바로 1개의 제곱수로 표현 가능
    if int(math.sqrt(N)) ** 2 == N :
        return 1
    
    TEMP:int = N
    while TEMP >= 8 :
        if TEMP % 4 == 0 :
            TEMP = TEMP >> 2
        else :
            break
    # 르장드르의 세 제곱수 정리에 의해 4^a(8b + 7)가 아닌 경우는 3개 이하의 제곱수의 합으로 가능합니다.
    # 그러나 만약 4^a(8b + 7)이면 제곱수 3개 이하가 불가능하므로 라그랑주의 네 제곱수 정리에 의해 4개입니다.
    if TEMP % 8 == 7 :
        return 4
    
    # 어려운 소인수분해(16563번) 소스 코드는 N이 작은 경우에 해당되나
    # 여기서는 N이 매우 크므로 큰 수 소인수분해(4149번) 소스 코드로 해야 합니다.
    NUMBER:int = N

    # 이제 N을 소인수분해 합니다.
    factor:list = []
    while NUMBER > 1 :
        divisor:int = pollardRho(NUMBER)
        factor.append(divisor)
        NUMBER = NUMBER // divisor

    # 오름차순으로 정렬합니다.
    factor.sort()
    
    four_n_plus_three:int = 0
    for i in range(len(factor)) :
        if factor[i] % 4 == 3 :
            four_n_plus_three += 1
            
    # 각 (4k+3) 소수별 지수를 세어, 한 번이라도 홀수인 소수가 있으면 2제곱수로 못 씁니다.
    # 이것을 무시한 경우 N = 21에서 반례가 발생합니다. 그러므로 아래 소스 코드로 합니다.
    for p, exp in Counter(factor).items() :
        if p % 4 == 3 and exp % 2 == 1 :
            return 3
    return 2

# 입력하고 알고리즘 실행하여 결과값을 출력합니다.
N:int = int(input().rstrip())
print(lagrange(N))