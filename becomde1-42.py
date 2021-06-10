def isfib(n):
    a=0
    b=1
    print(a,b ,end=" ")
    i=0
    for i in range(0,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input())
isfib(n)
    
