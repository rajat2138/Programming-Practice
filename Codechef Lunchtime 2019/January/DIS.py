for _ in range(int(input())):
    N=int(input())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))

    if A[0]!=0 or B[N-1]!=0 or A[N-1]!=B[0]:
        print('No')
        continue

    ans='Yes'
    for i in range(N):
        if i!= 0 and A[i]==0:
            ans='No'
            break
        if i!=N-1 and B[i]==0:
            ans='No'
            break
        if A[i]+B[i]<B[0] or A[i]+B[0]<B[i] or B[i]+B[0]<A[i]:
            ans='No'
            break
    print(ans)
