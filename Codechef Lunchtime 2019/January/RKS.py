for _ in range(int(input())):
    N,K= map(int, input().split())
    R=[False]*(N+1);C=[False]*(N+1)
    for i in range(K):
        r,c=map(int, input().split())
        R[r]=True;C[c]=True

    remainingRows=[]
    remainingColumns=[]
    for i in range(1, N+1):
        if not R[i]:
            remainingRows.append(i)
        if not C[i]:
            remainingColumns.append(i)
    P=len(remainingRows);S=str(P)
    for i in range(P):
        S+= ' '+ str(remainingRows[i])+ ' ' +str(remainingColumns[i])

    print(S)
