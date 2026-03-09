# 8878번 문제 : https://www.acmicpc.net/problem/8878
import sys
import math

input = sys.stdin.readline

K = 10

x, p = map(float, input().split())

# 예외 처리
if x == 0.0 or p == 0.0 :
    print("0.00000000")
    sys.exit(0)

r:float = x / 100.0
w:float = p / 100.0
s:float = 1.0 - r
q:float = 1.0 - w

# t = q/w > 1, logt = ln(t)
logt:float = math.log(q / w)

A:float = 1.0 + math.log(s) * (s / r) # ln(s) < 0
u:float = -math.log(s)                # = ln(1/s)

a0:float = A / logt
b0:float = (u / logt) - a0

def expected_profit(a:int, b:int) -> float :
    # P = (t^b - 1) / (t^(a+b) - 1)
    lb = logt * b
    lab = logt * (a + b)

    if lab < 50.0 :
        P = math.expm1(lb) / math.expm1(lab)
    else :
        elab = math.exp(-lab)
        P = (math.exp(-logt * a) - elab) / (1.0 - elab)

    return -s * b + (a + s * b) * P

best:float = 0.0

a_lo:int = max(1, int(math.floor(a0)) - K)
a_hi:int = max(1, int(math.ceil(a0)) + K)
b_lo:int = max(1, int(math.floor(b0)) - K)
b_hi:int = max(1, int(math.ceil(b0)) + K)

for a in range(a_lo, a_hi + 1) :
    for b in range(b_lo, b_hi + 1) :
        value = expected_profit(a, b)
        if value > best :
            best = value

print(f"{best:.8f}")