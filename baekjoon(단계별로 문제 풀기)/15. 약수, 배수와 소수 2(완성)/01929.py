# 1929번(소수 구하기) 문제 : https://www.acmicpc.net/problem/1929
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

M, N = map(int, input().split())

primes = sieve_of_eratosthenes(N)

for i in range(len(primes)) :
    if primes[i] >= M :
        print(primes[i])