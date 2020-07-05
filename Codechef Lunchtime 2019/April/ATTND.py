from collections import defaultdict as dd
for _ in range(int(input())):
    N = int(input())
    names=[]
    for i in range(N):
        names.append(tuple(input().split()))

    nameCount=dd(int)
    for i in range(N):
        nameCount[names[i][0]]+=1

    for i in range(N):
        if nameCount[names[i][0]]>1:
            print(names[i][0],names[i][1])
        else:
            print(names[i][0])
