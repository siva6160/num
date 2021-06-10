import math as m
num=int(input(""))
r=0
sum=0
temp=num
for i in range(1,num+1):
        r=num%10
        sum+=m.pow(r,3)
        num=num//10
        #print(r)
        #s=m.pow(r,3)
        #print(s)
        #sum=sum+s

#print(int(sum))
if(temp==sum):
    print("Arom Strong Number")
else:
    print("not")
