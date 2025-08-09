# 1991번(트리 순회) 문제 : https://www.acmicpc.net/problem/1991
import sys

input = sys.stdin.readline

# Class(객체) 선언 없이 이진 트리를 구현했습니다.

# 전위 순회
def preorder(node) :
    print(PARENT_NODES[node][0], end = "") # 1순위 : 부모 노드
    if PARENT_NODES[node][1] != None : # 2순위 : 왼쪽 자식 노드
        preorder(PARENT_NODES[node][1])
    if PARENT_NODES[node][2] != None : # 3순위 : 오른쪽 자식 노드
        preorder(PARENT_NODES[node][2])
    
# 중위 순회
def inorder(node) :
    if PARENT_NODES[node][1] != None : # 1순위 : 왼쪽 자식 노드
        inorder(PARENT_NODES[node][1])
    print(PARENT_NODES[node][0], end = "") # 2순위 : 부모 노드
    if PARENT_NODES[node][2] != None : # 3순위 : 오른쪽 자식 노드
        inorder(PARENT_NODES[node][2])
    
# 후위 순회
def postorder(node) :
    if PARENT_NODES[node][1] != None : # 1순위 : 왼쪽 자식 노드
        postorder(PARENT_NODES[node][1])
    if PARENT_NODES[node][2] != None : # 2순위 : 오른쪽 자식 노드
        postorder(PARENT_NODES[node][2])
    print(PARENT_NODES[node][0], end = "") # 3순위 : 부모 노드

N:int = int(input().rstrip())
PARENT_NODES:dict = dict()

for i in range(N) :
    parent, left_child, right_child = map(str, input().split())
    
    if left_child == '.' :
        left_child = None
    if right_child == '.' :
        right_child = None
    PARENT_NODES[parent] = [parent, left_child, right_child]
    
preorder(PARENT_NODES['A'][0])
print()
inorder(PARENT_NODES['A'][0])
print()
postorder(PARENT_NODES['A'][0])