# 10814번(나이순 정렬) 문제 : https://www.acmicpc.net/problem/10814
import sys

input = sys.stdin.readline

# 해시맵 없이 2차원 리스트로 구현한 것입니다.

N:int = int(input().rstrip())
member:list = []
for i in range(N) :
    age, name = map(str, input().split())
    member.append([int(age), name])

# 나이 기준으로 정렬(x[0])
# 여기서 이름은 먼저 들어온 순서대로 하므로 2순위 정렬은 없습니다.
member.sort(key = lambda x : x[0])

for i in range(len(member)) :
    print("{} {}".format(member[i][0], member[i][1]))