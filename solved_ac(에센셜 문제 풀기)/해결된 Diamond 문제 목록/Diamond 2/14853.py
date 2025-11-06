# 14853번(동전 던지기) 문제 : https://www.acmicpc.net/problem/14853
import sys
from decimal import Decimal, getcontext, ROUND_HALF_UP
sys.set_int_max_str_digits(1_000_000)

input = sys.stdin.readline

# 정밀도 20으로 설정합니다.
getcontext().prec = 20

# 0!부터 2002!까지 미리 구합니다.
# 즉, 다이나믹 프로그래밍으로 팩토리얼 캐시 재활용 합니다.
dp:list = [Decimal('1') for _ in range(2003)]

for i in range(1, 2002+1, 1) :
    dp[i] = dp[i-1] * Decimal(i)
    
# 이항 계수를 팩토리얼 캐시로 직접 구합니다.
def binomial_coefficient(n, k) :
    return dp[n] / (dp[k] * dp[n-k])
    
T:int = int(input().rstrip())

for _ in range(T) :
    n1, m1, n2, m2 = map(int, input().split())
    a:int = m1 + 1
    b:int = n1 - m1 + 1
    result:Decimal = Decimal('0')
    
    # 공식은 result = C0 * sigma(k = from 0 to m2) (n2+1)! / {(k)! * (n2+1 - k)!} * (a+k-1)! * (b+n2-k)!
    for k in range(0, m2+1, 1) :
        result += binomial_coefficient(n2+1, k) * dp[a+k-1] * dp[b+n2-k]
    # C0 = (a+b-1)! / {(a-1)!(b-1)!(a+b+n2)!}
    result *= dp[a+b-1]
    result /= dp[a-1] * dp[b-1] * dp[a+b+n2]
    print(result.quantize(Decimal('1e-10'), rounding=ROUND_HALF_UP))