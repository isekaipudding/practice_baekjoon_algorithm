# 1865번(웜홀) 문제 : https://www.acmicpc.net/problem/1865
import sys

input = sys.stdin.readline

# 벨만 포드 알고리즘 사용
def bellman_ford() :
    START_INDEX:int = 1 # 벨만 포드 알고리즘에서 맨 처음 노드를 1번 노드로 지정합니다.
    distance[START_INDEX] = 0 # 시작 노드의 누적된 거리값을 0으로 가정합니다.
    for i in range(1, N + 1, 1) :
        for j in range(len(graph)) :
            start:int = graph[j][0]
            end:int = graph[j][1]
            time:int = graph[j][2]
            # 핵심 알고리즘!
            if distance[end] > distance[start] + time :
                distance[end] = distance[start] + time
                if i == N :
                    print("YES")
                    return 
    print("NO")

T:int = int(input().rstrip())
for i in range(T) :
    N, M, W = map(int, input().split()) # 노드의 개수, 간선의 개수, 웜홀의 개수(이것도 결국 간선입니다.)
    
    graph:list = [] # 연결 그래프가 아니라는 힌트를 보고 아예 뜯어 고칩니다.
    distance:list = [10001 for _ in range(N + 1)] # 무한대가 아니라 10001로 했더니 정답 처리 되었습니다???
    
    for j in range(M) : # 웜홀이 아닌 정상적인 도로입니다.
        S, E, T = map(int, input().split()) # 출발 지점 S, 도착 지점 E, 걸리는 시간(가중치) T
        # 도로는 방향이 없으므로 가중치 있는 무방향 그래프입니다.
        graph.append([S, E, T])
        graph.append([E, S, T])
        
    for j in range(W) : # 웜홀입니다.
        S, E, T = map(int, input().split())
        # 조심해야 할 것은 문제에서 (단 도로는 방향이 없으며 웜홀은 방향이 있다.)라고 적혀 있습니다.
        # 즉, 웜홀은 (웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로)에 의해 출발 -> 도착 하나만 있습니다.
        # 따라서 웜홀은 가중치 있는 단방향 그래프입니다.
        graph.append([S, E, -T])
        # 그리고 (특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.)에 의해 가중치의 부호는 반전됩니다.
        
    bellman_ford() # 벨만 포드 알고리즘을 실행합니다.