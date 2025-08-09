# 11404번(플로이드) 문제 : https://www.acmicpc.net/problem/11404
import sys

input = sys.stdin.readline

# 플로이드 워셜 알고리즘 사용
def floyd() :
    for k in range(1, N + 1) :
        for i in range(1, N + 1) :
            for j in range(1, N + 1) :
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

N:int = int(input().rstrip()) # 정점의 개수(도시 개수)
M:int = int(input().rstrip()) # 간선의 개수(버스 경로 개수)

# 도시가 100개 뿐이므로 인접 행렬로 선언합니다.
# 이 때 float("INF")는 양의 무한대를 의미합니다.
graph:list = [[float("INF") for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M) :
    u, v, w = map(int, input().split()) # 출발 지점, 도착 지점, 비용 입력
    # 이 때 단방향 그래프이므로 graph[v][u] 추가는 없습니다. 
    # 그리디 알고리즘 사용(여러 개의 경로 중 가장 비용이 저렴한 경로 선택)
    if graph[u][v] > w :
        graph[u][v] = w
        
floyd() # 최단 경로 검색 시작

# 출력 형식에 맞게 출력합니다.
for i in range(1, N + 1) : 
    for j in range(1, N + 1) : 
        if graph[i][j] == float("INF") : # 만약 도달할 수 없으면
            print(0, end=' ')
        else : # 한 번 도달한 적 있다면
            print(graph[i][j], end=' ')
    print() # 출력 형식을 지키기 위해 추가
    # i for문과 j for 문 사이에 넣어야 했는데 j for문 안에 들어가서 출력 형식이 잘못되었습니다.
    # 위치를 수정해서 형식을 바로 잡습니다.