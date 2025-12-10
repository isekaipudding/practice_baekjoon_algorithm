# 4948번(베르트랑 공준) 문제 : https://www.acmicpc.net/problem/4948
import sys

input = sys.stdin.readline

# 아아... 이것은 『에라토스테네스의 체』라고 한다. 소수를 쉽게 구해주지.
def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= max_num):
        if (is_prime[p]):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if is_prime[p]]

while True :
    N:int = int(input().rstrip())
    if N == 0 :
        break
    count:int = 0
    primes = sieve_of_eratosthenes(2*N)
    for i in range(len(primes)) :
        if primes[i] > N :
            count = len(primes) - i
            print(count)
            break