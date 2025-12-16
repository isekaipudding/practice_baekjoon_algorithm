# 13174번(괄호) 문제 : https://www.acmicpc.net/problem/13174
import sys

input = sys.stdin.readline

MOD = 1_000_000_007

# 에디토리얼 : https://higstudev.github.io/BOJ13174/
# 증명이 너무 까다로워서 결론부터 말하자면
# 답은 sigma(from k = ceil(N/2) to N) K^k * (N_C_k - N_C_(k+1)) % MOD

N, K = map(int, input().split())

factorial:list = [1 for _ in range(N+1)]
for i in range(1, N + 1) :
    factorial[i] = factorial[i - 1] * i % MOD

# 팩토리얼의 모듈러 곱셈 역원 리스트
invfactorial = [1 for _ in range(N + 1)]
# MOD가 소수이므로 페르마의 소정리로 모듈러 곱셈 역원을 바로 구할 수 있습니다.
invfactorial[N] = pow(factorial[N], MOD - 2, MOD)
for i in range(N, 0, -1) :
    invfactorial[i - 1] = invfactorial[i] * i % MOD

# 이항 계수 구하는 함수
def nCr(n, r) :
    if r < 0 or r > n :
        return 0
    return factorial[n] * invfactorial[r] % MOD * invfactorial[n - r] % MOD

start:int = (N + 1) // 2 # ceil(N/2)
powK:int = pow(K, start, MOD)

result:int = 0
for k in range(start, N + 1) :
    count:int = (nCr(N, k) - nCr(N, k + 1)) % MOD
    result = (result + count * powK) % MOD
    powK = powK * K % MOD

print(result)