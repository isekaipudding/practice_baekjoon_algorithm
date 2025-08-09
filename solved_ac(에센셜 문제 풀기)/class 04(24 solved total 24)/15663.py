# 15663번(N과 M(9)) 문제 : https://www.acmicpc.net/problem/15663
import sys

input = sys.stdin.readline

# 중복된 수열을 제외하기 위해 사전 자료형을 활용했습니다.

def backtracking(start_index) :
    if len(stack) == M :
        print(" ".join(map(str, stack)))
        return
    else : 
        for i in range(start_index, len(dict_keys)) :
            if NUMBER_DICT[dict_keys[i]] > 0 :
                NUMBER_DICT[dict_keys[i]] -= 1
                stack.append(dict_keys[i])
                backtracking(0)
                stack.pop()
                NUMBER_DICT[dict_keys[i]] += 1

N, M = map(int, input().split())
L:list = list(map(int, input().split()))
L.sort()

NUMBER_DICT:dict = dict()
NUMBER_DICT[L[0]] = 1

for i in range(1, len(L), 1) :
    if L[i] == L[i-1] :
        NUMBER_DICT[L[i]] += 1
    else :
        NUMBER_DICT[L[i]] = 1
        
dict_keys:list = list(NUMBER_DICT.keys())
stack:list = []
backtracking(0)