size=list(map(int,input().split()))
p=1
for i in range(size[0]):
    if i<size[0]//2:
        print('-'*((size[1] - (3 * p)) // 2)+".|."*p+'-'*((size[1] - (3 * p)) // 2),end="")
        p += 2
        print()
    elif i==size[0]//2:
        print('-'*((size[1]-7)//2)+"WELCOME"+'-'*((size[1]-7)//2))
    else:
        if (p*3)==size[1]:
            p-=2
        print('-' * ((size[1] - (3 * p)) // 2) + ".|." * p + '-' * ((size[1] - (3 * p)) // 2), end="")
        p -= 2
        print()
