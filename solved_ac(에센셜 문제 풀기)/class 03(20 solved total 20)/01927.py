# 1927번(최소 힙) 문제 : https://www.acmicpc.net/problem/1927
import sys
from queue import PriorityQueue # 이 문제는 우선순위 큐 알고리즘 문제입니다.

input = sys.stdin.readline

T:int = int(input().rstrip())
min_Heap = PriorityQueue()

# status:bool=False #출력에서 엔터키를 원활하게 처리하기 위한 변수... 이었으나 파이썬에서는 생략
for i in range(T) :
    IN:int = int(input().rstrip())
    
    if IN == 0 :
        if min_Heap.qsize() == 0 :
            print(0)
        else :
            print(min_Heap.get())
            # 우선순위 큐는 기본적으로 우선순위가 따로 주어지지 않으면 가장 작은 값을 반환한 뒤 삭제.
    if IN != 0 :        
        min_Heap.put(IN)