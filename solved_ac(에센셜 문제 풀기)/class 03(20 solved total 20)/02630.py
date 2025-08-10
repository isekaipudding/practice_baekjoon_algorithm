# 2630번(색종이 만들기) 문제 : https://www.acmicpc.net/problem/2630
import sys

input = sys.stdin.readline

# 4779번(칸토어 집합)에서 영감을 얻어 초기식과 점화식을 저만의 방식으로 따로 유도했습니다.
# 재귀 함수 및 DP 알고리즘의 장점은 초기식과 점화식만 알면 쉽게 풀립니다.
# 그러나 단점은 그 초기식과 점화식 구하기가 너무 어렵습니다...

def counting_papers(row, col, size, color) :
    if size == 2 : # 믿기지 않겠지만 이게 초기식입니다.
        L:list = []
        L.append(colors[row][col]) # 1구역 단일 셀
        L.append(colors[row][col + 1]) # 2구역 단일 셀
        L.append(colors[row + 1][col]) # 3구역 단일 셀
        L.append(colors[row + 1][col + 1]) # 4구역 단일 셀
        
        count:int = 0
        for i in range(4) :
            if L[i] == color : # 만약 해당 색깔과 일치하면
                count += 1
                
        if count == 4 : # 만약 4개 단일 셀이 모두 해당 색깔과 일치하면
            return -1 # -1로 반환합니다.
        else : # 그게 아니라면
            return count # 색칠된 영역 개수만큼 반환합니다.
    # 점화식입니다.
    else :
        half_size = size // 2
        top_left = counting_papers(row, col, half_size, color)
        top_right = counting_papers(row, col + half_size, half_size, color)
        bottom_left = counting_papers(row + half_size, col, half_size, color)
        bottom_right = counting_papers(row + half_size, col + half_size, half_size, color)
        
        if top_left == -1 and top_right == -1 and bottom_left == -1 and bottom_right == -1 :
            if size == N : # 만약 모든 cell의 색깔이 해당 색깔로 칠해져 있다면
                return 1 # 1로 반환합니다.
            else : # 그 외의 경우는 -1로 반환합니다.
                return -1
        else : # 4개의 구역 중 하나라도 -1이 아닌 경우는 절대값 합으로 반환합니다.
            return abs(top_left) + abs(top_right) + abs(bottom_left) + abs(bottom_right)

N:int = int(input().rstrip())
colors:list = [list(map(int, input().split())) for _ in range(N)]

print(counting_papers(0, 0, N, 0)) # 하얀색 종이 개수 구하기
print(counting_papers(0, 0, N, 1)) # 파란색 종이 개수 구하기