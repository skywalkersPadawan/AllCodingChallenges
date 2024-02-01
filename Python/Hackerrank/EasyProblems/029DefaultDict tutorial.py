from collections import defaultdict

diction = defaultdict(list)
groupOne, groupSecond = map(int, input().split())
for i in range(groupOne):
    diction[input()].append(str(i + 1))
for j in range(groupSecond):
    print(" ".join(d[input()]) or -1)
