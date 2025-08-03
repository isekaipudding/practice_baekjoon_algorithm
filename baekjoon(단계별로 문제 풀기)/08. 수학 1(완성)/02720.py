# 2720번(세탁소 사장 동혁) 문제 : https://www.acmicpc.net/problem/2720
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    change_in_cents = int(input().rstrip())

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    quarters = change_in_cents // 25
    change_in_cents %= 25

    dimes = change_in_cents // 10
    change_in_cents %= 10

    nickels = change_in_cents // 5
    change_in_cents %= 5

    pennies = change_in_cents

    result = [quarters, dimes, nickels, pennies]
    print(" ".join(map(str,result)))