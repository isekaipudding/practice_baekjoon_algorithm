# 1238번(파티) 문제 : https://www.acmicpc.net/problem/1238
import heapq # 다익스트라 알고리즘을 사용할 때 힙 자료구조(우선순위 큐) 같이 사용하면 시간 복잡도가 많이 감소합니다.
import sys

input = sys.stdin.readline

MAX:int = 1000 * 10000 * 100 # 최대 학생 수 * 최대 단방향 도로 개수 * 최대 소요 시간

# 다익스트라 알고리즘 사용
# 다익스트라 알고리즘은 BFS 알고리즘에서 응용된 것입니다.
def dijkstra(start, end) :
    queue = [(0,start)] 
    distance = [MAX for _ in range(N+1)] # 누적 거리값 리스트는 다익스트라 알고리즘 실행될 때마다 초기화합니다.
    distance[start] = 0 # 다익스트라 알고리즘에서 출발 지점의 누적 거리값은 0으로 합니다.
    
    while queue : 
        now, next = heapq.heappop(queue)
        if now > distance[next] :
            continue
        for i in graph[next] :
            time = now + i[1]
            if distance[i[0]] > time :
                distance[i[0]] = time
                heapq.heappush(queue, (time, i[0]))
            
    return distance[end]

N, M, X = map(int, input().split())
graph:list = [[] for _ in range(N+1)] # 노드의 개수가 많으므로 인접 리스트로 선언

for i in range(M) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 단방향 그래프이므로 하나만 추가합니다.
    
max_distance:int = 0 # 초기값을 0으로 합니다.
for i in range(1, N+1, 1) :
    from_house_to_party:int = dijkstra(i, X) # 집에서 파티장(노드 번호 X)으로 가는데 걸리는 최단 경로
    from_party_to_house:int = dijkstra(X, i) # 파티장(노드 번호 X)에서 집으로 가는데 걸리는 최단 경로
    # 모든 사람들은 집에서 파티장 그리고 파티장에서 집으로 돌아가야 하므로 둘을 더해야 합니다.
    TEMP:int = from_house_to_party + from_party_to_house
    # 최대 최단 거리를 갱신합니다.
    max_distance = max(max_distance, TEMP)

print(max_distance)