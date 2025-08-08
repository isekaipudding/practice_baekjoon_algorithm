# 2166번(다각형의 면적) 문제 : https://www.acmicpc.net/problem/2166
from collections import deque
import sys

input = sys.stdin.readline

# 다각형의 넓이 알고리즘 기초 문제입니다.
# 신발끈 공식을 응용하면 다각형 넓이 공식으로 유도됩니다.

N:int = int(input().rstrip())

axis_of_x = deque()
axis_of_y = deque()

for i in range(N) : 
    x, y = map(int, input().split())
    axis_of_x.append(x)
    axis_of_y.append(y)
    
result:int = 0
for i in range(N) : 
    # 다각형의 넓이 알고리즘 사용(신발끈 공식 응용)
    result += axis_of_x[0] * axis_of_y[1] - axis_of_x[1] * axis_of_y[0]
    axis_of_x.rotate(-1)
    axis_of_y.rotate(-1)
    
print(0.5 * abs(result))