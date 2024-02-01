from itertools import combinations_with_replacement

s, k = map(str, input().split())
S = sorted(s)
k = int(k)

for e in list(combinations_with_replacement(S, k)):
    print(*e, sep="")
