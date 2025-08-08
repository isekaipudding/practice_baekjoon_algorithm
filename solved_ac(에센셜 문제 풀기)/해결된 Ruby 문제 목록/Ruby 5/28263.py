# 28263번(하이퍼 가짜 초코릿) : https://www.acmicpc.net/problem/28263
import sys
import random
from collections import Counter
import time

input = sys.stdin.readline

# 테스트한 결과 0.2초 ~ 1.6초로 3.5초 안에 들어가는 것을 확인했습니다.

# 타이머 시작
# start = time.time()

# 참고 자료 : https://en.wikipedia.org/wiki/Fermat%27s_little_theorem (코코 정리)
# 참고 자료 : https://en.wikipedia.org/wiki/Carmichael_number (가찌 초코릿 수)
# 참고 자료 : https://en.wikipedia.org/wiki/Square-free_integer (제곱 ㄴㄴ 수)

# 참고 소스 코드 출처 : https://c0degolf.github.io/posts/beakjoon/28263/28263/
# 큰 수 소인수분해(4149번) 소스 코드를 재활용합니다.

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
    
# 소인수 리스트로 반환합니다.
def divisors(N) -> list :
    # 1. Pollard Rho 를 이용해 소인수 리스트 pf 에 담기
    pf:list = []
    while N > 1 :
        divisor:int = pollardRho(N)
        pf.append(divisor)
        N = N // divisor

    # 2. 소인수별 개수 세기
    count = Counter(pf)

    # 3. 지수 조합으로 모든 약수 생성
    divs:list = [1]
    for p, exp in count.items() :
        # 기존의 divs 리스트에 있는 각 요소에 대해 p^0, p^1, ... p^exp를 각각 곱한다.
        divs = [d * (p**k) for d in divs for k in range(exp+1)]

    return sorted(divs)

# 리스트 원소들을 모두 곱합니다.
def products(L) -> int :
    result:int = 1
    for number in L :
        result *= number
    return result

# 휴리스틱 알고리즘을 통해 소수 데이터를 추출합니다.
def search() -> int :
    while True :
        heuristics:list = random.sample(choco_number_list, 5)
        pi:int = products(heuristics)

        try :
            inv = pow(pi, -1, N)
        except :
            continue

        right[inv] = pi

        if inv in right and pi % N in left :
            return pi * left[pi % N]

        heuristics:list = random.sample(choco_number_list, 6)
        pi:int = products(heuristics)

        try :
            inv = pow(pi, -1, N)
        except :
            continue

        left[inv] = pi

        if inv in left and pi % N in right :
            return pi * right[pi % N]

# 결과 목록과 가짜 초코릿 수를 찾아줍니다.
def find() -> tuple :
    while True :
        TEMP:int = search()
        factors = []
        for choco_number in choco_number_list :
            if TEMP % choco_number == 0 :
                factors.append(choco_number)

        if len(factors) == 11 :
            return factors, TEMP
        
# 기존 N은 2^8 * 3^6 * 5^4 * 7^2 * 11^1입니다.
# 그러나 N이 클수록 정확도가 높아지므로 휴리스틱 적용하여 N의 값을 증가시킵니다.(약수 개수 증가)
# 1. 기본 소인수와 지수
exponents:dict = {
    2: 8,
    3: 6,
    5: 4,
    7: 2,
    11: 1,
}

# 임의의 소수 하나를 추출합니다.(휴리스틱 적용)
sample_prime:list = random.sample([2, 3, 5, 7, 11], 1)

# N을 증가시킵니다.
exponents[sample_prime[0]] += 1

# 최종 N 계산합니다.
N:int = 1
for p, e in exponents.items() :
    N *= p**e
    
L:list = divisors(N)
choco_number_list = []

for value in L :
    value += 1
    if is_prime(value) and gcd(value, N) == 1 :
        if 10 ** 7 <= value and value < 10 ** 8 :
            choco_number_list.append(value)

left:dict = dict()
right:dict = dict()

while True :
    try :
        # 1. 랜덤 탐색으로 조합 찾기
        result, fake_choco_number = find()

        # 2. 검증 : 범위
        if not all(10**7 <= p < 10**8 for p in result) :
            raise ValueError("range check failed")
        # 3. Korselt’s criterion
        if not all((fake_choco_number - 1) % (p - 1) == 0 for p in result) :
            raise ValueError("Korselt check failed")
        # 4. 최종 모듈로 체크
        if fake_choco_number % N != 1 :
            raise ValueError("final mod check failed")

        # 모두 통과했으면 루프 탈출
        break

    except Exception as e :
        # 실패했을 때 left/right 사전 초기화 해주고
        left.clear()
        right.clear()
        # 다시 while True 로 돌아가서 find() 를 재실행
        continue

# 최종 출력
print(*result)

# 타이머 종료 및 출력
"""
end = time.time()
print(f"Elapsed time: {end - start:.3f} sec", file=sys.stderr)
"""