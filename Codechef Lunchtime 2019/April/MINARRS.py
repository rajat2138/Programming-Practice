for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    bitCountOne=[0]*31
    bitCountZero=[0]*31
    bitsum=0
    for a in A:
        bitsum+=int(bin(a)[2:][::-1])
    binStr=''
    for bit in str(bitsum):
        if int(bit)>=N//2+1:
            binStr+='1'
        else:
            binStr+='0'

    X=int(binStr, 2)
    minSum=0
    for a in A:
        minSum+=X^a
    print(minSum)
