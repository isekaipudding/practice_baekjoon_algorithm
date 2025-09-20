import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
Result = -1
if N < 3 :
    Result = -1
else :
    Remainder = N%15
    if Remainder == 0 :
        Result = N//5
    if Remainder == 1 :
        Result = 4+(N-16)//5
    if Remainder == 2 :
        Result = 5+(N-17)//5
    if Remainder == 3 :
        Result = 1+(N-3)//5
    if Remainder == 4 :
        if N == 4 :
            Result = -1
        else :
            Result = 5+(N-19)//5
    if Remainder == 5 :
        Result = 1+(N-5)//5
    if Remainder == 6 :
        Result = 2+(N-6)//5
    if Remainder == 7 :
        if N == 7 :
            Result = -1
        else :
            Result = 6+(N-22)//5
    if Remainder == 8 :
        Result = 2+(N-8)//5
    if Remainder == 9 :
        Result = 3+(N-9)//5
    if Remainder == 10 :
        Result = 2+(N-10)//5
    if Remainder == 11 :
        Result = 3+(N-11)//5
    if Remainder == 12 :
        Result = 4+(N-12)//5
    if Remainder == 13 :
        Result = 3+(N-13)//5
    if Remainder == 14 :
        Result = 4+(N-14)//5
print(Result)

# (3<=n&&n<=17)(switch문으로 해결... 할려고 했으나 파이썬에서는 switch 안 되니 if문으로 대체)
# 3 -> 3kg 1개 -> 1 (mod 15==3)
# 4 -> 불가능 -> -1 (mod 15==4)
# 5 -> 5kg 1개 -> 1 (mod 15==5)
# 6 -> 3kg 2개 -> 2 (mod 15==6)
# 7 -> 불가능 -> -1 (mod 15==7)
# 8 -> 3+5 -> 3kg 1개 5kg 1개 -> 2 (mod 15==8)
# 9 -> 3kg 3개 -> 3 (mod 15==9)
# 10 -> 5kg 2개 -> 2 (mod 15==10)
# 11 -> 6+5 -> 3kg 2개, 5kg 1개 -> 3 (mod 15==11)
# 12 -> 3kg 4개 -> 4 (mod 15==12)
# 13 -> 3+5+5 -> 3kg 1개, 5kg 2개 -> 3 (mod 15==13)
# 14 -> 9+5 -> 3kg 3개, 5kg 1개 -> 4 (mod 15==14)
# 15 -> 5kg 3개 -> 3 (mod 15==0)
# 16 -> 6+5+5 -> 3kg 2개, 5kg 2개 -> 4(mod 15==1)
# 17 -> 12+5 -> 3kg 4개, 5kg 1개 -> 5 (mod 15==2)

# 19 -> 9+10 -> 3kg 3개, 5kg 2개 -> 5
# 22 -> 12+10 -> 3kg 4개, 5kg 2개 -> 6