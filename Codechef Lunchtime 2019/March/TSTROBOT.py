for _ in range(int(input())):
    N,X = map(int, input().split())
    path=input()

    position= set()
    position.add(X)
    for p in path:
        if p=='L':
            X-=1
        else:
            X+=1
        position.add(X)
    print(len(position))
