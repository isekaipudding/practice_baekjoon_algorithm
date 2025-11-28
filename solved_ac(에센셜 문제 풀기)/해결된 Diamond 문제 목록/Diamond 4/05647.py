# 5647번(연속 합) 문제 : https://www.acmicpc.net/problem/5647
import sys

input = sys.stdin.readline

# 참고 블로그 : https://memoacmicpc.tistory.com/entry/백준-5647번-연속-합

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
    return [p for p in range(max_num+1) if is_prime[p]]

# q가 최대 10^14이므로 그의 제곱근인 10^7으로 미리 소수들을 구합니다.
primes:list = sieve_of_eratosthenes(10_000_000)
    
while True :
    try :
        N:int = int(input().rstrip())
        # 탈출 조건
        if N < 1 :
            break
        while N % 2 == 0 :
            N //= 2
            
        result:int = 1
        
        # 에라토스테네스의 체만으로 밀러-라빈, 폴라드 로 없이 구현합니다.
        for p in primes :
            # 모두 다 찾을 필요 없이 필요한 소수들만 활용합니다.
            if p * p > N :
                break
            exponent:int = 0
            while N % p == 0 :
                exponent += 1
                N //= p
            result *= 2 * exponent + 1
        # 만약 N > 10^7인데 소수인 경우 예외 처리.
        if N != 1 :
            result *= 3
            
        print(2 * result)
    except :
        pass