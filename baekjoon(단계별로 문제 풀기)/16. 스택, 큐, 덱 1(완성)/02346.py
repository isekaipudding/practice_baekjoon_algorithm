# 2346번(풍선 터뜨리기) 문제 : https://www.acmicpc.net/problem/2346
import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
queue = deque(enumerate(map(int, input().split())))
numbers = []

while len(queue) > 0 :
    index, paper = queue.popleft()
    numbers.append(index + 1)

    if paper > 0:
        queue.rotate(-(paper - 1))
    elif paper < 0:
        queue.rotate(-paper)

print(' '.join(map(str, numbers)))