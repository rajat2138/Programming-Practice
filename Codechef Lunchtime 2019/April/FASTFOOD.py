for _ in range(int(input())):
    N=int(input())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    profit=sum(A)
    maxprofit=profit
    for i in range(N-1,-1,-1):
        profit=profit-A[i]+B[i]
        maxprofit=max(maxprofit, profit)
    print(maxprofit)
