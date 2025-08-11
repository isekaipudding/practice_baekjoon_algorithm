# 1978번(소수 찾기) 문제 : https://www.acmicpc.net/problem/1978
import sys

input=sys.stdin.readline

# 이번엔 에라토스테네스의 체 알고리즘 + 이진 탐색 알고리즘을 혼합해서 최적화 합니다.

# 에라토스테네스의 체 알고리즘
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        # 해당 수가 아직 지워지지 않았다면
        if is_prime[p]:
            # 해당 수의 모든 배수를 지웁니다.
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    # 소수 목록 생성
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_numbers

# 1부터 1000까지의 소수를 구합니다.
primes = sieve_of_eratosthenes(1000)

N:int = int(input().rstrip())
numbers:list = list(map(int, input().split()))

# 이진 탐색 알고리즘 사용
def binary_search(array, target):
    START_INDEX, END_INDEX = 0, len(array) - 1
    while START_INDEX <= END_INDEX:
        MID_INDEX = (START_INDEX + END_INDEX) // 2
        if array[MID_INDEX] < target:
            START_INDEX = MID_INDEX + 1
        elif array[MID_INDEX] > target:
            END_INDEX = MID_INDEX - 1
        else:
            return True  # 타겟을 찾음
    return False  # 타겟을 찾지 못함

count:int = 0
for i in range(N):
    if binary_search(primes, numbers[i]):  # 이진 탐색 호출
        count += 1
    
print(count)