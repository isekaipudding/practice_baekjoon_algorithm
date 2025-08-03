# 11005번(진법 변환 2) 문제 : https://www.acmicpc.net/problem/11005
import sys

input = sys.stdin.readline

N, B = map(int, input().split())

MaxMultiplier:int = -1
Temp:int = N

while Temp > 0 :
    Temp //= B
    MaxMultiplier += 1

Temp:int = N
result:str = ""

for i in range(MaxMultiplier, -1, -1) :
    Dight:int = Temp // (B**i)
    Temp %= B**i
    if 0 <= Dight and Dight <= 9 :
        result += str(Dight)
    elif 10 <= Dight and Dight <= 35 :
        result += chr(Dight - 10 + 65)
        
print(result)