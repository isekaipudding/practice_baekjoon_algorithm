# 17104번(골드바흐 파티션 2) : https://www.acmicpc.net/problem/17104
import sys
input = sys.stdin.readline

MAX_NUMBER = 1000000
is_prime = [True] * (MAX_NUMBER + 1)
primes = []

def sieve_of_eratosthenes():
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_NUMBER**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, MAX_NUMBER+1, i):
                is_prime[j] = False
    for p in range(2, MAX_NUMBER+1):
        if is_prime[p]:
            primes.append(p)

# NTT 설정
mod = 998244353
prim_root = 3

def modpow(a, e=mod-2):
    r = 1
    while e:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r

def ntt(a, invert):
    n = len(a)
    # 비트 반전 순서
    rev = [0] * n
    for i in range(n):
        rev[i] = (rev[i>>1] >> 1) | ((i & 1) * (n >> 1))
    for i in range(n):
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]
    # Cooley–Tuk 알고리즘
    length = 1
    while length < n:
        # primitive n-th root 계산
        wlen = modpow(prim_root, (mod - 1) // (length * 2))
        if invert:
            wlen = modpow(wlen)
        for i in range(0, n, length * 2):
            w = 1
            for j in range(length):
                u = a[i + j]
                v = a[i + j + length] * w % mod
                a[i + j] = (u + v) % mod
                a[i + j + length] = (u - v + mod) % mod
                w = w * wlen % mod
        length <<= 1
    if invert:
        inv_n = modpow(n)
        for i in range(n):
            a[i] = a[i] * inv_n % mod

def multiply(A, B):
    need = len(A) + len(B) - 1
    n = 1
    while n < need:
        n <<= 1
    fa = A + [0] * (n - len(A))
    fb = B + [0] * (n - len(B))
    ntt(fa, False)
    ntt(fb, False)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % mod
    ntt(fa, True)
    return fa[:need]

sieve_of_eratosthenes()
# FFT 길이: 2^20
N = 1 << 20
A = [0] * N
B = [0] * N
# 홀수 소수만 표시
for p in primes:
    if p == 2:
        continue
    idx = (p - 1) // 2
    A[idx] = B[idx] = 1

# 한 번만 NTT
C = multiply(A, B)

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 4:
        print(1)
    elif n % 2 == 0:
        ways = C[n//2 - 1]
        print((ways + 1)//2)
    else:
        print(0)