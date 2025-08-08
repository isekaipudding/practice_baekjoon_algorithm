# 17646번(제곱수의 합 2(More Huge)) 문제 : https://www.acmicpc.net/problem/17646
import sys
import random
import math
from collections import Counter
from typing import Tuple

input = sys.stdin.readline

# 제곱수의 합 more huge(17633번) 문제에 제출했던 소스 코드를 재활용합니다.
# 최소 개수가 2개일 때가 가장 어려웠습니다. 진짜 생소한 알고리즘으로 구현하는 것이 정말 매우 어렵습니다.

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

# Tonelli-Shanks 알고리즘: 모듈러 방정식 r^2 ≡ residue (mod prime)의 해를 구합니다.
def tonelli_shanks(residue: int, prime: int) -> int:
    assert pow(residue, (prime - 1) // 2, prime) == 1, "해가 존재하지 않습니다"
    # prime-1을 q * 2^s 형태로 분해
    q: int = prime - 1
    exponent_s: int = 0
    while q & 1 == 0:
        q //= 2
        exponent_s += 1
    # 2차 비잔여(quadratic non-residue) z 찾기
    candidate: int = 2
    while pow(candidate, (prime - 1) // 2, prime) != prime - 1:
        candidate += 1
    # 초기값 설정
    iterations: int = exponent_s
    c_value: int = pow(candidate, q, prime)
    t_value: int = pow(residue, q, prime)
    root: int = pow(residue, (q + 1) // 2, prime)

    # 알고리즘 반복 수행
    while True :
        if t_value == 0 :
            return 0
        if t_value == 1 :
            return root
        # t_value^(2^i) == 1이 되는 최소 i 찾기
        i: int = 1
        t2i: int = (t_value * t_value) % prime
        while t2i != 1 :
            t2i = (t2i * t2i) % prime
            i += 1
        # 변수 갱신
        adjustment: int = pow(c_value, 1 << (iterations - i - 1), prime)
        iterations = i
        c_value = (adjustment * adjustment) % prime
        t_value = (t_value * c_value) % prime
        root = (root * adjustment) % prime

# Cornacchia 알고리즘: p ≡ 1 (mod 4)인 소수에 대해 x^2 + y^2 = p를 만족하는 (x,y)를 구합니다.
def cornacchia(prime: int) -> Tuple[int, int]:
    # 먼저 t^2 ≡ -1 (mod prime) 해를 구함
    t_candidate: int = tonelli_shanks(prime - 1, prime)
    # 유클리드 호제법과 유사한 과정으로 축소
    remainder0: int = prime
    remainder1: int = t_candidate
    while remainder1 * remainder1 > prime:
        remainder0, remainder1 = remainder1, remainder0 % remainder1
    x_value: int = remainder1
    y_squared: int = prime - x_value * x_value
    y_value: int = int(math.isqrt(y_squared))
    return (x_value, y_value)

# 복소수 곱셈: (u0 + i*u1) * (v0 + i*v1)
def multiply_complex(u: Tuple[int,int], v: Tuple[int,int]) -> Tuple[int,int]:
    u0, u1 = u
    v0, v1 = v
    return (u0 * v0 - u1 * v1,
            u0 * v1 + u1 * v0)

# 복소수 거듭제곱: (base)^(exponent)
def pow_complex(base: Tuple[int,int], exponent: int) -> Tuple[int,int]:
    result: Tuple[int,int] = (1, 0)
    current: Tuple[int,int] = base
    e: int = exponent
    while e > 0:
        if e & 1:
            result = multiply_complex(result, current)
        current = multiply_complex(current, current)
        e >>= 1
    return result

# 두 제곱수의 합 표현: N = x^2 + y^2 형태로 표현 가능한 (x,y)를 반환합니다.
def sum_of_two_squares(N: int) -> Tuple[int,int]:
    # 소인수분해
    factor_counts: Counter[int,int] = Counter()
    temp: int = N
    while temp > 1:
        divisor: int = pollardRho(temp)
        factor_counts[divisor] += 1
        temp //= divisor

    # 복소수 표현 초기화 (1 + 0i)
    complex_rep: Tuple[int,int] = (1, 0)
    for prime_factor, exponent_count in factor_counts.items():
        if prime_factor == 2:
            # 2^exp 처리
            if exponent_count % 2:
                complex_rep = multiply_complex(complex_rep, (1, 1))
            scale: int = 2 ** (exponent_count // 2)
            complex_rep = (complex_rep[0] * scale, complex_rep[1] * scale)
        elif prime_factor % 4 == 3:
            # (4k+3) 소수는 짝수 차수만 허용
            scale: int = prime_factor ** (exponent_count // 2)
            complex_rep = (complex_rep[0] * scale, complex_rep[1] * scale)
        else:
            # (4k+1) 소수: Cornacchia 후 거듭제곱
            x0, y0 = cornacchia(prime_factor)
            cx, cy = pow_complex((x0, y0), exponent_count)
            complex_rep = multiply_complex(complex_rep, (cx, cy))

    x_final, y_final = complex_rep
    return (abs(x_final), abs(y_final))

# 아무리 여러 번 해도 계속 TLE 떠서 블로그를 참고하여 메모이제이션(캐시)를 추가합니다.
# 전역 캐시 선언
lagrange_cache:dict[int, int] = {}
sum_two_squares_cache:dict[int, tuple[int,int]] = {}

def find_squares(NUMBER) -> list[int] :
    # 최소 개수를 구합니다.
    COUNT:int = lagrange(NUMBER)
    # 최수 개수를 출력합니다.
    print(COUNT)
    L:list = []
    # N = w^2 + x^2 + y^2 + z^2 = 4^a(8b + 7)인 경우(르장드르의 세 제곱수 정리 성립 안 된 경우)
    # 4^a(8b + 7) = 4^a(8b + 6) + 4^a
    # x^2 + y^2 + z^2 = 4^a(8b + 6) <- 자동적으로 르장드르의 세 제곱수 정리 성립
    # w^2 = 4^a = (2^a)^2 -> w = 2^a
    # N = N - w^2
    if COUNT == 4 :
        TEMP:int = NUMBER
        k:int = 0
        while TEMP >= 8 :
            if TEMP % 4 == 0 :
                k += 1
                TEMP = TEMP >> 2
            else :
                break
        w:int = 2 ** k
        NUMBER -= w ** 2
        L.append(w)
        COUNT -= 1
        
    # 와... COUNT == 3에서 TLE가 발생하네요... 와 미치겠다...
    # COUNT == 3: Legendre + 인수분해 기반 수론적 하강법
    if COUNT == 3 :
        # 1) 인수분해
        TEMP:int = NUMBER
        factor_list: list[int] = []
        while TEMP > 1 :
            divisor:int = pollardRho(TEMP)
            factor_list.append(divisor)
            TEMP //= divisor
        factor_dict = Counter(factor_list)
        # 2) multiple 변수와 new_n 계산
        multiple:int = 1
        new_n:int = 1
        for prime, exponent in factor_dict.items():
            multiple *= pow(prime, exponent // 2)
            if exponent % 2 :
                new_n *= prime
        # 3) z 찾기 : new_n - z^2 가 두 제곱수 합인지 (lagrange == 2)
        z:int = 1
        while lagrange(new_n - z*z) != 2 :
            z += 1
        # 4) 스케일 복원
        z *= multiple
        # 남은 값 업데이트
        NUMBER -= z*z
        L.append(z)
        COUNT -= 1

    # 인수분해 + “두 제곱수 합” 캐싱 + 복소수 항등식
    # 사실 이것도 블로그 내용을 참고했습니다.
    if COUNT == 2 :
        # 1) 소인수분해 (pollardRho 결과는 내부 메모이제이션)
        factor:Counter = Counter()
        TEMP:int = NUMBER
        while TEMP > 1 :
            divisor:int = pollardRho(TEMP)
            factor[divisor] += 1
            TEMP //= divisor

        # 2) (4k+3) 소수 짝수 차수만 분리
        result_complex:tuple = (1, 0)
        for prime, exponent in list(factor.items()) :
            if prime % 4 == 3 :
                scale:int = prime ** (exponent // 2)
                result_complex = (result_complex[0] * scale,
                                  result_complex[1] * scale)
                factor[prime] = 0

        # 3) 나머지 인수 → sum_of_two_squares 캐싱
        for prime, exponent in factor.items() :
            if exponent == 0 :
                continue
            pe:int = prime ** exponent
            if pe not in sum_two_squares_cache :
                sum_two_squares_cache[pe] = sum_of_two_squares(pe)
            x, y = sum_two_squares_cache[pe]
            a, b = result_complex
            # 항등식으로 복소수 곱셈
            result_complex = (a*x - b*y, a*y + b*x)

        xf, yf = result_complex
        L.extend([abs(xf), abs(yf)])
        COUNT -= 2
        
    # 만약 완전 거듭제곱인 경우 N = x^2이므로 L에 x 추가
    if COUNT == 1 :
        L.append(int(math.sqrt(NUMBER)))
        COUNT -= 1
        
    L.sort()
    
    return L

# 입력하고 알고리즘 실행하여 결과값을 출력합니다.
N:int = int(input().rstrip())
result:list = find_squares(N)
print(*result)