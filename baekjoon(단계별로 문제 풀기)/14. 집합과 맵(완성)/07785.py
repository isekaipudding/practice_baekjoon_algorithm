# 7785번(회사에 있는 사람) 문제 : https://www.acmicpc.net/problem/7785
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

# 리스트로 해서 시간 초과가 발생했으니 사전으로 하고 value는 논리형으로 합니다.
RESULTS:dict = dict()

for i in range(N) :
    name, InOut = map(str, input().split())
    if InOut == "enter" :
        RESULTS[name] = True
    elif InOut == "leave" :
        RESULTS[name] = False

for i in sorted(RESULTS.keys(), reverse=True) :
    if RESULTS[i] == True :
        print(i)