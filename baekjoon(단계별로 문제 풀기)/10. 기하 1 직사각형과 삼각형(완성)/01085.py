# 1085번(직사각형에서 탈출) : https://www.acmicpc.net/problem/1085
import sys

input = sys.stdin.readline

X, Y, W, H = map(int, input().split())
Distance:list=[X, W-X, Y, H-Y]
print(min(Distance))