def print_formatted(num):
    sp=len(bin(num)[2:])
    for i in range(1,num+1):
        print(int(i).__format__(str(len(str(num)))), oct(i)[2:].rjust(sp), hex(i)[2:].rjust(sp), bin(i)[2:].rjust(sp))

if __name__=='__main__':
    n=int(input())
    print_formatted(n)