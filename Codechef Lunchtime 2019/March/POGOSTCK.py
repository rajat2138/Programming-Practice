for i in range(int(input())):
    N,K= map(int, input().split())
    A=list(map(int, input().split()))
    score=[0]*N
    for i in range(K):
        score[N-1-i]=A[N-i-1]
    for i in range(N-1-K, -1, -1):
        score[i]=A[i]+score[i+K]
    print(max(score))
