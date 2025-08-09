# 1753번(최단경로) 문제 : https://www.acmicpc.net/problem/1753
import sys
import heapq

input = sys.stdin.readline

def dijkstra(start_node, graph, num_nodes) :
    distances = [float('inf')] * (num_nodes + 1)
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (거리, 노드)

    while priority_queue :
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 현재 노드까지의 거리보다 더 큰 경우 무시
        if current_distance > distances[current_node] :
            continue
        
        for neighbor, weight in graph[current_node] :
            distance = current_distance + weight
            
            # 현재 노드를 거쳐서 가는 것이 더 빠른 경우 업데이트
            if distance < distances[neighbor] :
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 입력 받기
Node, Edge = map(int, input().split())
START_NODE = int(input().rstrip())

# 그래프 초기화
graph = [[] for _ in range(Node + 1)]

for _ in range(Edge):
    A_NODE, B_NODE, A_TO_B_VALUE = map(int, input().split())
    graph[A_NODE].append((B_NODE, A_TO_B_VALUE))

# 다익스트라 알고리즘 실행
shortest_distances = dijkstra(START_NODE, graph, Node)

# 결과 출력
for i in range(1, Node + 1) :
    if shortest_distances[i] == float('inf') :
        print("INF")
    else:
        print(shortest_distances[i])