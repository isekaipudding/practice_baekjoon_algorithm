# 11444번(피보나치 수 6) 문제 : https://www.acmicpc.net/problem/11444
import sys

input = sys.stdin.readline

def matrix_mult(A, B, mod) : 
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]

def matrix_pow(M, n, mod) :
    result = [[1, 0], [0, 1]]
    base = M
    
    while n > 0 :
        if n % 2 == 1 :
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        n //= 2
        
    return result

def fibonacci_mod(n, mod) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1, mod)
    return result[0][0]

n:int=int(input().rstrip()) #뷁 이런 실수를 하다니
remainder = 1000000007

result = fibonacci_mod(n, remainder)
print(result)