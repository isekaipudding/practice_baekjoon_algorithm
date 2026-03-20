# 17468번(N! mod P (3)) 문제 : https://www.acmicpc.net/problem/17468
import sys
from decimal import Decimal, setcontext, Context, MAX_PREC, MAX_EMAX

# 빠른 입출력 및 재귀 해제
sys.setrecursionlimit(1 << 20)
# 파이썬 정수-문자열 변환 자릿수 제한 해제 (보안 제한 해제)
sys.set_int_max_str_digits(0)
input = sys.stdin.readline

# Decimal 모듈의 정밀도를 최대치로 설정 (NTT 엔진 활성화)
setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX))

# 참고 소스 코드는 ishs311317님 소스 코드(100969078) 참고했습니다.
# 해당 소스 코드를 제 방식으로 다시 작성했습니다.
# 다시 봐도 다항식을 거대 정수로 변환하는 것에 진심으로 감탄합니다.

def get_inverse(n:int, p:int) -> int :
    """페르마의 소정리를 이용한 모듈러 역원 계산"""
    return pow(n, p - 2, p)

def kronecker_multiply_decimal(poly_a:list, poly_b:list, pad_size:int = 26) -> list :
    """다항식을 거대 정수로 치환하여 C-level에서 초고속으로 곱하는 함수"""
    d:int = len(poly_a) - 1
    f_str:str = f"0{pad_size}d"
    
    # 리스트를 통째로 문자열로 뭉쳐서 Decimal로 변환 (리스트 연산 최소화)
    dec_a:Decimal = Decimal("".join(format(x, f_str) for x in poly_a))
    dec_b:Decimal = Decimal("".join(format(x, f_str) for x in poly_b))
    
    dec_c:Decimal = dec_a * dec_b
    
    total_length:int = pad_size * (len(poly_a) + len(poly_b) - 1)
    str_c:str = format(dec_c, f"0{total_length}f")
    
    # 원본 코드의 핵심 최적화: 전체가 아닌 딱 필요한 구간(d+1 ~ 4d+2)만 언패킹!
    start_idx:int = (d + 1) * pad_size
    end_idx:int = (4 * d + 2) * pad_size
    
    return [int(str_c[i:i + pad_size]) for i in range(start_idx, end_idx, pad_size)]

def extend_polynomial(current_f:list, p:int) -> list :
    """f(x)를 f(x+d) 꼴로 확장하는 함수 (리스트 연산 최소화)"""
    d:int = len(current_f) - 1
    next_f:list = current_f.copy()
    
    fact:list = [1]
    inv_fact:list = []
    inv_mul:list = []
    
    # 팩토리얼 계산
    for i in range(1, 4 * d + 2) :
        fact.append((fact[-1] * i) % p)
        
    inv_fact.append(get_inverse(fact[-1], p))
    
    for i in range(4 * d + 1, 0, -1) :
        inv_fact.append((inv_fact[-1] * i) % p)
    inv_fact.reverse()
    
    inv_mul.append(1)
    for i in range(1, 4 * d + 2) :
        inv_mul.append((fact[i - 1] * inv_fact[i]) % p)
        
    c0:int = fact[d]
    base_a:list = []
    
    # 다항식 세팅
    for i in range(d + 1) :
        val:int = (current_f[i] * inv_fact[i]) % p
        val = (val * inv_fact[d - i]) % p
        if (d - i) % 2 != 0 :
            val = -val
        base_a.append(val % p)
        
    # 크로네커 치환으로 필요한 부분만 계산해서 받아옴
    conv_result:list = kronecker_multiply_decimal(base_a, inv_mul, 26)
    
    # 슬라이딩 윈도우 방식으로 리스트 접근을 최소화하며 값 추가
    for i in range(d + 1, 4 * d + 2) :
        c0 = (c0 * i) % p
        c0 = (c0 * inv_mul[i - d - 1]) % p
        next_f.append((conv_result[i - d - 1] * c0) % p)
        
    return next_f

def double_degree(current_f:list, p:int) -> list :
    """f_2d(x) = f_d(2x) * f_d(2x+1) 원리를 적용하여 차수를 2배로 늘림"""
    d:int = (len(current_f) - 2) // 4
    next_f:list = []
    for i in range(2 * d + 1) :
        next_f.append((current_f[2 * i] * current_f[2 * i + 1]) % p)
    return next_f

def process_next_step(current_f:list, p:int) -> list :
    """위의 두 함수를 합성하여 한 스텝 전진"""
    return double_degree(extend_polynomial(current_f, p), p)

# 변수명 오류 방지를 위해 소문자 n, p로 수정
n, p = map(int, input().split())

if n >= p :
    print(0)
    sys.exit(0)
    
# 초기 함숫값: f_1(0) = 1, f_1(1) = 2
f_values:list = [1, 2]

target_block_size:int = 1
step_count:int = 0

# 블록 사이즈 계산 (v * v < n)
while target_block_size * target_block_size < n :
    target_block_size *= 2
    step_count += 1
    
# 정확히 계산된 step_count만큼 분할 정복 진행
for _ in range(step_count) :
    f_values = process_next_step(f_values, p)
    
# 최종 조립
blocks:int = n // target_block_size
result:int = 1

for i in range(blocks) :
    result = (result * f_values[i]) % p
    
# 남은 자투리 계산
for i in range(blocks * target_block_size + 1, n + 1) :
    result = (result * i) % p
    
print(result)