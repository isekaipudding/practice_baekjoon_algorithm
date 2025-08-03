# 2941번(크로아티아 알파벳) 문제 : https://www.acmicpc.net/problem/2941
import sys

input = sys.stdin.readline

input_string:str = input().rstrip()

count:int = 0
for i in range(len(input_string)) :
    if i == 1 :
        if ((input_string[0] == 'c' and input_string[1] == '=') or
            (input_string[0] == 'c' and input_string[1] == '-') or
            (input_string[0] == 'd' and input_string[1] == '-') or
            (input_string[0] == 'l' and input_string[1] == 'j') or
            (input_string[0] == 'n' and input_string[1] == 'j') or
            (input_string[0] == 's' and input_string[1] == '=') or
            (input_string[0] == 'z' and input_string[1] == '=')):
            count += 1
    elif i > 1 :
        if ((input_string[i - 1] == 'c' and input_string[i] == '=') or
            (input_string[i - 1] == 'c' and input_string[i] == '-') or
            (input_string[i - 1] == 'd' and input_string[i] == '-') or
            (input_string[i - 1] == 'l' and input_string[i] == 'j') or
            (input_string[i - 1] == 'n' and input_string[i] == 'j') or
            (input_string[i - 1] == 's' and input_string[i] == '=') or
            (input_string[i - 1] == 'z' and input_string[i] == '=')):
            count += 1
        if i >= 2 and input_string[i - 2] == 'd' and input_string[i - 1] == 'z' and input_string[i] == '=' :
            count += 1

print(len(input_string) - count)