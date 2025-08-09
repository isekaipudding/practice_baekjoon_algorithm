# 13549번(숨바꼭질 3) 문제 : https://www.acmicpc.net/problem/13549
from collections import deque
import sys

input = sys.stdin.readline

visited:list = [False for _ in range(100001)] # index 0부터 100000까지 False로 이루어진 방문 여부 리스트

# 이 문제는 자바스크립트에서 나오는 DOM에서 등장하는 (형제 노드)를 고려해서 구현했습니다.
# 원래 이 문제는 다익스트라 알고리즘으로 풀어야 하는 것이 맞으나 X*2 형제 노드를 고려해도 풀립니다.

def bfs(N, K) :
    count:int = 0 # 트리 구조에서 깊이(depth)를 의미합니다.
    
    queue = deque()
    TEMP:int = N
    if TEMP == 0 : # 반례 : 0 10인 경우 무한 루프가 발생하여 메모리 초과 발생
        queue.append(TEMP)
        visited[TEMP] = True
    elif TEMP > 0 :
        while TEMP <= 100000 : # 루트의 형제 노드 추가
            queue.append(TEMP)
            visited[TEMP] = True
            TEMP = TEMP << 1
    
    queue.append(-1) # 이 코드는 이 문제에서 정말 중요한 역할을 합니다.
    
    while queue :
        TEMP:int = queue.popleft()
        
        if TEMP == K : # 해당 값을 찾았으면 count 반환합니다.
            return count
        if TEMP == -1 : # -1의 의미는 현재 depth에 존재하는 원소가 더이상 없음을 의미합니다.
            count += 1 # 다음 depth로 이동하므로 count 1 증가해야 합니다.
            queue.append(-1)
            continue # 아래 조건문들을 무시하기 위해 continue
        if TEMP - 1 == 0 : # 만약 노드 번호가 0번인 경우가 있고
            if visited[TEMP - 1] == False : # 아직 방문하지 않았다면
                queue.append(TEMP - 1)
                visited[TEMP - 1] = True
        elif TEMP - 1 > 0 : # 만약 X > 0이고
            if visited[TEMP - 1] == False : # 아직 방문하지 않았다면
                SECOND_TEMP:int = TEMP - 1 # 임시값으로 저장하고
                while SECOND_TEMP <= 100000 : # 범위 내에서
                    queue.append(SECOND_TEMP) # 자식 노드 및 그 자식 노드의 형제 노드도 추가하고
                    visited[SECOND_TEMP] = True # 방문했음을 체크한 뒤
                    SECOND_TEMP = SECOND_TEMP << 1 # 형제 노드 X * 2도 고려합니다.
                    
        if TEMP + 1 <= 100000 : # 만약 x+1이 범위를 벗어나지 않으면 같은 원리를 적용합니다.
            if visited[TEMP + 1] == False :
                SECOND_TEMP:int = TEMP + 1
                while SECOND_TEMP <= 100000 :
                    queue.append(SECOND_TEMP)
                    visited[SECOND_TEMP] = True
                    SECOND_TEMP = SECOND_TEMP << 1
    
    return -1 # 어떠한 방법으로도 도달할 수 없는 경우 -1로 반환

N, K = map(int, input().split())
print(bfs(N, K))