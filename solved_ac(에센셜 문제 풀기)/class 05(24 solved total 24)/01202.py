# 1202번(보석 도둑) 문제 : https://www.acmicpc.net/problem/1202
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

boseok:list = []
gabang:list = []

for _ in range(N) :
    M, V = map(int, input().split())
    boseok.append((M, V))
for _ in range(K) :
    gabang.append(int(input().rstrip()))
    
boseok.sort()
gabang.sort()

result:int = 0
TEMP:list = []

for i in range(len(gabang)) :
    while boseok and boseok[0][0] <= gabang[i] :
        heapq.heappush(TEMP, -boseok[0][1])
        heapq.heappop(boseok)
    if TEMP :
        result -= heapq.heappop(TEMP)

print(result)