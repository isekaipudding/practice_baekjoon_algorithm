# 13705번(Ax+Bsin(x)=C) 문제 : https://www.acmicpc.net/problem/13705
import sys
from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_HALF_UP

input = sys.stdin.readline

# 이 문제는 유도 과정이 더럽다... 하지만 결과는 아름답다.

# 충분히 여유 있는 정밀도
getcontext().prec = 50

A, B, C = map(int, input().split())

# 고정밀 PI (Decimal)
PI = Decimal('3.14159265358979323846264338327950288419716939937510')
TWO_PI = PI * 2

def sin_decimal(x: Decimal) -> Decimal:
    # (1) 2π로 나머지 연산해서 각도를 줄인다 (0 <= t < 2π)
    q = (x / TWO_PI).to_integral_value(rounding=ROUND_FLOOR)
    t = x - q * TWO_PI

    # (2) 대칭성을 이용해 [-π, π]로 더 줄인다
    if t > PI :
        t -= TWO_PI

    # (3) 테일러 전개로 sin(t) 근사
    term = t   # 현재 항
    res = t    # 누적합
    i = 3      # 다음 분모는 (2*1)*(2*1+1)=2*3=6 -> 3부터 시작
    sign = -1  # 부호 : -, +, -, ...

    eps = Decimal('1e-40')  # 충분히 작은 cutoff
    while True :
        term = term * t * t / (Decimal(i - 1) * Decimal(i))
        res += Decimal(sign) * term
        if term.copy_abs() < eps :
            break
        i += 2
        sign *= -1

    return res

def f(x:Decimal) -> Decimal :
    # f(x) = A*x + B*sin(x) - C
    return A_d * x + B_d * sin_decimal(x) - C_d

A_d = Decimal(A)
B_d = Decimal(B)
C_d = Decimal(C)

# 이진 탐색 구간 설정
lo = Decimal('0')
hi = (C_d + B_d) / A_d  # 위에서 증명한 상한

# 단조 증가 함수이므로 전형적인 이진 탐색
for _ in range(200) :
    mid = (lo + hi) / 2
    if f(mid) > 0 :
        hi = mid
    else :
        lo = mid

result = (lo + hi) / 2

# 소수점 여섯째 자리까지 반올림해서 출력
result_out = result.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
print(result_out)

"""
우선 f(x) = A*x + B*sin(x) - C로 정의합니다.
여기서 구해야 하는 답은 f(x) = 0을 만족하는 x입니다.

f(x)를 미분하면 f'(x) = A + B*cos(x)가 됩니다.
여기서 항상 -1 <= cos(x) <= 1을 만족하므로
A - B <= f'(x) <= A + B
그런데 문제 조건에서 0 < B ≤ A ≤ 100,000가 존재합니다.
즉, B <= A이며 이는 0 <= A - B를 의미합니다.
따라서 0 <= f'(x)를 만족하며 이는 항상 단조 증가한다는 것을 알 수 있습니다.
따라서 x의 해는 유일함을 보장 받습니다.

이번엔 이진 탐색 구간을 확인해야 합니다.
A*x + B*sin(x)에서 항상 -1 <= sin(x) <= 1이므로
A*x - B <= A*x + B*sin(x) <= A*x + B
여기서 A*x + B*sin(x) = C이므로
A*x - B <= C <= A*x + B

여기서 각각 x의 범위를 따로 구하면 다음과 같은 결과가 나옵니다.
(1) A*x - B <= C
-> x <= (C + B)/A
(2) A*x + B >= C
-> x >= (C - B)/A

따라서 x 탐색 범위는 다음과 같습니다.
(C - B) / A <= x <= (C + B) / A
혹시나 모르니 안전하게 탐색하기 위해
0 <= x <= (C + B) / A
이렇게 해서 lo = 0, hi = (C + B) / A로 설정합니다.
아까 전에 해의 유일성을 증명했으므로 이진 탐색을 하여 식에 대입하고 재탐색 등을 하면 답이 나옵니다.

이렇게 해서 이 문제를 해결할 수 있습니다.

아 맞다. 테일러 급수를 이용하여
sin t = t − t^3/3! + t^5/5! − t^7/7! + ...
이 공식을 활용하면 시간 복잡도 개선할 수 있습니다.(성능 향상 UP!)
"""