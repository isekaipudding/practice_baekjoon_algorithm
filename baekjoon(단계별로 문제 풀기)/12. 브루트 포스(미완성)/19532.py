# 19532번(수학은 비대면강의입니다) 문제 : https://www.acmicpc.net/problem/19532
import sys

input=sys.stdin.readline

# 크라메르 공식을 사용하면 굉장히 쉽게 풀립니다.
# ax+by=c
# dx+ey=f
# 이렇게 되어 있죠?

# 이것을 행렬식으로 표현합니다.
#      |c b|
#      |f e|
# x = ------- = (ce-bf)/(ae-bd)
#      |a b|
#      |d e|

#      |a c|
#      |d f|
# y = ------- = (af-cd)/(ae-bd)
#      |a b|
#      |d e|

A, B, C, D, E, F = map(int, input().split())
X:int = int((C*E - B*F) / (A*E - B*D))
Y:int = int((A*F - C*D) / (A*E - B*D))
print("{} {}".format(X,Y))