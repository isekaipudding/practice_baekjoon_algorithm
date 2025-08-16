# 1067번(이동) : https://www.acmicpc.net/problem/1067
import sys
input = sys.stdin.readline

# Python으로 CRT/NTT 방식으로 FFT 문제를 해결합니다.
# NTT 설정 (mod=998244353, primitive root=3)
MOD = 998244353
PRIM_ROOT = 3

def modpow(a, e, mod=MOD):
    r = 1
    while e:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r

def ntt(a, invert):
    n = len(a)
    # 비트 반전
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 1
    while length < n:
        wlen = modpow(PRIM_ROOT, (MOD - 1) // (length * 2))
        if invert:
            wlen = modpow(wlen, MOD - 2)
        i = 0
        while i < n:
            w = 1
            for j in range(i, i + length):
                u = a[j]
                v = a[j + length] * w % MOD
                a[j] = (u + v) % MOD
                a[j + length] = (u - v + MOD) % MOD
                w = w * wlen % MOD
            i += length * 2
        length <<= 1

    if invert:
        inv_n = modpow(n, MOD - 2)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD

def multiply(A, B):
    need = len(A) + len(B) - 1
    n = 1
    while n < need:
        n <<= 1
    fa = A[:] + [0] * (n - len(A))
    fb = B[:] + [0] * (n - len(B))
    ntt(fa, False)
    ntt(fb, False)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD
    ntt(fa, True)
    return fa[:need]

N:int = int(input().rstrip())
X:list = list(map(int, input().split()))
Y:list = list(map(int, input().split()))

# A = X를 두 번 이어붙임 (길이 2N)
A:list = X + X
# B = Y를 뒤집음 (길이 N)
B:list = Y[::-1]

# 선형 합성곱 리스트 길이는 2N + N - 1 = 3N - 1
C:list = multiply(A, B)

# 유효 구간 : [N-1, 2N-1] (총 N개)
# 이 구간의 최댓값이 X와 Y의 원형 정렬 중 최대값
result = max(C[N-1:2*N])

print(result)