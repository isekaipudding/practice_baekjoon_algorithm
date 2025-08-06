# 1978번(소수 찾기) : https://www.acmicpc.net/problem/1978
import sys

input = sys.stdin.readline

# 에라토스테네스의 체 알고리즘 적용. 앞으로 자주 사용되는 알고리즘.
def sieve_of_eratosthenes(limit) :
    is_prime = [True] * (limit + 1) # 소수 여부를 저장할 리스트 초기화
    p = 2 # 첫 번째 소수

    while (p**2 <= limit) :
        if is_prime[p]==True : # p가 소수이면
            for i in range(p**2, limit + 1, p) : # p의 배수를 제거
                is_prime[i] = False
        p += 1

    primes = []
    for p in range(2, limit + 1) : # 1은 소수가 아니므로 초기값은 2
        if is_prime[p]==True :
            primes.append(p) # 소수를 리스트에 추가

    return primes

# 1000 이하의 모든 소수를 구합니다
limit = 1000
prime_numbers = sieve_of_eratosthenes(limit)


N:int = int(input().rstrip())
numbers = list(map(int,input().split()))

count:int = 0
for i in range(N) :
    if numbers[i] in prime_numbers :
        count += 1

print(count)