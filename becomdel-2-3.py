num=int(input())
rev=0
if num>0:
    for i in range(num):
        r=num%10
        if r>0:
            rev=(rev*10)+r
            num=num//10
print(rev)
