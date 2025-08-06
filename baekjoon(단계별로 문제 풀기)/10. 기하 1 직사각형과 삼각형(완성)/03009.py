# 3009번(네 번째 점) 문제 : https://www.acmicpc.net/problem/3009
import sys

input = sys.stdin.readline

X_AXIS:list = []
Y_AXIS:list = []
for i in range(3) :
    X, Y = map(int, input().split())
    X_AXIS.append(X)
    Y_AXIS.append(Y)
X_AXIS.sort()
Y_AXIS.sort()
    
result_x = 0
result_y = 0

if X_AXIS[1] == X_AXIS[0] :
    result_x = X_AXIS[2]
elif X_AXIS[1] == X_AXIS[2] :
    result_x = X_AXIS[0]
    
if Y_AXIS[1] == Y_AXIS[0] :
    result_y = Y_AXIS[2]
elif Y_AXIS[1] == Y_AXIS[2] :
    result_y = Y_AXIS[0]

print("{} {}".format(result_x, result_y))