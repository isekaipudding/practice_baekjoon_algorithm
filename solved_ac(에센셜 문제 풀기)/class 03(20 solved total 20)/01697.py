# 1697번(숨바꼭질) 문제 : https://www.acmicpc.net/problem/1697
from collections import deque
import sys

input = sys.stdin.readline

visited:list = [False for _ in range(100001)] # index 0부터 100000까지 False로 이루어진 방문 여부 리스트

def bfs(N, K) :
    count:int = 0 # 트리 구조에서 깊이(depth)를 의미합니다.
    
    queue = deque()
    queue.append(N)
    visited[N] = True
    
    queue.append(-1) # 이 코드는 이 문제에서 정말 중요한 역할을 합니다.
    
    while queue :
        TEMP:int = queue.popleft()
        
        if TEMP == K : # 해당 값을 찾았으면 count 반환합니다.
            return count
        if TEMP == -1 : # -1의 의미는 현재 depth에 존재하는 원소가 더이상 없음을 의미합니다.
            count += 1 # 다음 depth로 이동하므로 count 1 증가해야 합니다.
            queue.append(-1)
            continue # 아래 조건문들을 무시하기 위해 continue
        if TEMP - 1 >= 0 : # 만약 x-1이 범위를 벗어나지 않고
            if visited[TEMP - 1] == False : # 아직 방문하지 않았다면
                queue.append(TEMP - 1) # 원소를 추가하고
                visited[TEMP - 1] = True # 방문했음을 기록합니다.
        if TEMP + 1 <= 100000 : # 만약 x+1이 범위를 벗어나지 않으면 같은 원리를 적용합니다.
            if visited[TEMP + 1] == False :
                queue.append(TEMP + 1)
                visited[TEMP + 1] = True
        if TEMP * 2 <= 100000 : # 만약 x*2이 범위를 벗어나지 않으면 같은 원리를 적용합니다.
            if visited[TEMP * 2] == False :
                queue.append(TEMP * 2)
                visited[TEMP * 2] = True
    
    return -1 # 어떠한 방법으로도 도달할 수 없는 경우 -1로 반환

N, K = map(int, input().split())
print(bfs(N, K))