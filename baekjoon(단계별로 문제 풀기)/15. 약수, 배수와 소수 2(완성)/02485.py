# 2485번(가로수) 문제 : https://www.acmicpc.net/problem/2485
import sys

input = sys.stdin.readline

# 아... 이것은 유클리드 호제법이라는 것이다. gcd는 최대공약수, lcm은 최소공배수를 의미하지.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

T:int = int(input().rstrip())

# 나무 위치들을 저장하고 sort 실시
numbers:list = []
for i in range(T) :
    TREE:int = int(input().rstrip())
    numbers.append(TREE)
numbers.sort()

# 여기가 핵심입니다. 인접한 두 나무의 거리를 구하고 이를 list 안에 저장합니다.
different:list = []
for i in range(0, len(numbers)-1, 1) :
    different.append(numbers[i+1] - numbers[i])

# 이 알고리즘은 여러 개의 최대공약수를 구하는 알고리즘입니다.
GCD_A = different[0]
for i in range(1,len(different),1) :
    GCD_A = gcd(GCD_A,different[i])

# 처음 지점부터 마지막 지점까지 이론상 가능한 최대 나무 개수 : (numbers[len(numbers)-1]-numbers[0])//GCD_A+1
# 현재 존재하는 나무의 개수 : len(numbers)
# 이 둘을 빼면 필요한 나무의 개수가 구해집니다.
result:int = (numbers[len(numbers)-1] - numbers[0]) // GCD_A + 1 - len(numbers)
print(result)