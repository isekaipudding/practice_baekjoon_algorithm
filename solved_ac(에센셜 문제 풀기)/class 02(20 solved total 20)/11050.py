# 11050번(이항 계수 1) 문제 : https://www.acmicpc.net/problem/11050
import sys

input = sys.stdin.readline

n, r = map(int, input().split())

numerator:int = 1 # 분자
denominator:int = 1 # 분모
result:int = 1 # 결과값 (nC0일때의 결과값)
for i in range(r) :
    numerator = n - i # 예시로 n=5인 경우 5,4,3,2,1
    denominator = i + 1 # 예시로 n=5인 경우 1,2,3,4,5
    result = result * numerator // denominator # 예시로 n=5, r=3인 경우 (5/1)*(4/2)*(3/3)
    
print(result)

"""
1. result *= numerator // denominator
2. result = result * numerator // denominator
1번 식과 2번 식은 연산 순서가 다르므로 엄연히 다른 식입니다!
예시로 n=10, r=3인 경우 1번 식과 2번 식의 결과는 다음과 같습니다.

[1번 식]
1번째 루프 : 10//1 연산을 먼저 하고 1*10 연산을 한 뒤 result에 대입
2번째 루프 : 9//2 연산을 먼저 하고 10*4 연산을 한 뒤 result에 대입
3번째 루프 : 8//3 연산을 먼저 하고 40*2 연산을 한 뒤 result에 대입
최종적으로 result는 80으로 출력

[2번 식]
1번째 루프 : 1*10 연산을 먼저 하고 10//1 연산을 한 뒤 result에 대입
2번째 루프 : 10*9 연산을 먼저 하고 90//2 연산을 한 뒤 result에 대입
3번째 루프 : 45*8 연산을 먼저 하고 360//3 연산을 한 뒤 result에 대입
최종적으로 result는 120으로 출력

실제로 nCr에서 10C3의 값은 120이므로 2번 식을 적용하는 것이 옳습니다.
"""