# 9063번(대지) 문제 : https://www.acmicpc.net/problem/9063
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

X_AXIS = []
Y_AXIS = []
for i in range(T) :
    X, Y = map(int, input().split())
    X_AXIS.append(X)
    Y_AXIS.append(Y)
    
X_AXIS.sort()
Y_AXIS.sort()

AREA:int = (X_AXIS[len(X_AXIS)-1]-X_AXIS[0]) * (Y_AXIS[len(Y_AXIS)-1]-Y_AXIS[0])
print(AREA)