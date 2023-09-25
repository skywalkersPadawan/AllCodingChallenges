import re

T = int(input())
for i in range(T):
    try:
        print(bool(re.compile(input())))
    except:
        print("False")
