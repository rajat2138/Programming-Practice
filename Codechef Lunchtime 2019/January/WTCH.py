-for _ in range(int(input())):
    N=int(input())
    S= input()
    if N==1:
        if S=='0':
            print(1)
        else:
            print('0')
        continue
    if N==2:
        if S=='00':
            print('1')
        else:
            print('0')
        continue
    S=list(S)
    ans=0
    if S[0]=='0' and S[1]=='0':
        S[0]='1'
        ans+=1
    for i in range(2, N-1):
        if S[i]!='1' and S[i-1]!='1' and S[i+1]!='1':
            S[i]='1'
            ans+=1
    if S[N-1]=='0' and S[N-2]=='0':
        ans+=1
    print(ans)
