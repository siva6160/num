num=int(input(""))
rev=0
for i in range(num):
    r=num%10
    rev=(rev*10)+r
    num=num//10
print(rev)
