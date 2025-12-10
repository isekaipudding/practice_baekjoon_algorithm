# 4134번(다음 소수) 문제 : https://www.acmicpc.net/problem/4134
import sys
import math

input = sys.stdin.readline

def is_prime(n):
    # n이 소수인지 여부를 확인하기 위한 소수 판별
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_min_prime_greater_than_x(x):
    # x보다 크거나 같은 수부터 시작
    candidate = x
    while True:
        if is_prime(candidate):  # 소수 확인
            return candidate  # 찾은 최소 소수를 반환
        candidate += 1  # 다음 수로 이동

# 테스트 케이스 수 입력 받기
T:int=int(input().rstrip())

for i in range(T) :
    # 사용자로부터 입력 받기
    x = int(input().rstrip())

    # 주어진 x보다 큰 최소 소수 찾기
    min_prime = find_min_prime_greater_than_x(x)

    # 결과 출력
    print(min_prime)