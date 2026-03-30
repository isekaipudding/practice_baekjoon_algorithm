# 11689번(GCD(n, k) = 1) : https://www.acmicpc.net/problem/11689
import sys
import math

input = sys.stdin.readline

# N을 입력합니다.
N:int = int(input().rstrip())

# 이제 N을 소인수분해 합니다. 다른 점은 리스트가 아닌 집합으로 해서 중복된 소인수는 제거합니다.
S:set = set()
factor:int = 2
TEMP:int = N
while int(math.sqrt(TEMP)) >= factor and TEMP > 1 :
    if TEMP % factor == 0 :
        S.add(factor)
        TEMP //= factor  
    else :
        factor += 1
if TEMP > 1 :
    S.add(TEMP)

L:list = list(S)
L.sort()

# 오일러 피 함수를 적용하기 위해 분자와 분모를 구합니다.
numerator:int = 1 # 분자
denominator:int = 1 # 분모
for prime in L :
    numerator *= prime - 1
    denominator *= prime
    
# 오일러 피 함수를 적용하여 결과값을 출력합니다.
print(N * numerator // denominator)