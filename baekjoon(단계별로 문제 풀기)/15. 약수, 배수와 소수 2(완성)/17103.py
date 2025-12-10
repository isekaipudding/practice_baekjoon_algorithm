# 17103번(골드바흐 파티션) 문제 : https://www.acmicpc.net/problem/17103
import sys

input = sys.stdin.readline

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

def find_goldbach_partitions(n, primes):
    count = 0
    for prime in primes:
        if prime > n // 2:
            break
        if (n - prime) in primes_set:
            count += 1
    return count

max_num = 1000000
primes = sieve_of_eratosthenes(max_num)
primes_set = set(primes)

t = int(input().rstrip())
results = []

for _ in range(t):
    n = int(input().rstrip())
    results.append(find_goldbach_partitions(n, primes))

print('\n'.join(map(str, results)))