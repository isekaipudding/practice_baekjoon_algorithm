# 2805번(나무 자르기) 문제 : https://www.acmicpc.net/problem/2805
import sys
import math

input = sys.stdin.readline

# 이 문제는 이진 탐색 알고리즘이 아닌 다른 방식으로 해결합니다.
# HashMap 자료구조를 활용하여 그리디 알고리즘으로 해결합니다.

N, NEED_TREE_HEIGHT = map(int, input().split())
tree_height_list:list = list(map(int, input().split()))
tree_height_list.sort() # 원활한 사전 원소 대입을 위해 오름차순으로 정렬합니다.

dict_of_trees:dict = dict()
MAX_TEMP:int = tree_height_list[0]
dict_of_trees[0] = 0 # index 오류를 방지하기 위해 0:0을 추가합니다.
dict_of_trees[MAX_TEMP] = 1 # 초기값 설정
key_list:list = [0, MAX_TEMP] # index 오류를 방지하기 위해 0을 추가합니다.
for i in range(1, N, 1) :
    if MAX_TEMP == tree_height_list[i] :
        dict_of_trees[MAX_TEMP] += 1
    else :
        MAX_TEMP = tree_height_list[i]
        key_list.append(MAX_TEMP)
        dict_of_trees[MAX_TEMP] = 1
        
result:int = key_list[-1]
while dict_of_trees : # 브루트 포스 알고리즘 사용
    if NEED_TREE_HEIGHT > (key_list[-1] - key_list[-2]) * dict_of_trees[key_list[-1]] : # 그리디 알고리즘 사용
        NEED_TREE_HEIGHT -= (key_list[-1] - key_list[-2]) * dict_of_trees[key_list[-1]]
        dict_of_trees[key_list[-2]] += dict_of_trees[key_list[-1]]
        del dict_of_trees[key_list[-1]]
        key_list.pop()
        result = key_list[-1]
    else :
        result -= int(math.ceil(NEED_TREE_HEIGHT / dict_of_trees[key_list[-1]]))
        break
        
print(result)