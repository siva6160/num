import math
def isarmstrong(num):
    r=0
    sum=0
    temp=num
    for i in range(1,num+1):
        r=num%10
        sum+=math.pow(r,3)
        num=num//10
    if(temp==sum):
        print("Arm Strong Number")
    else:
        print("Not Arm Strong Number")
num=int(input(""))
isarmstrong(num)
    
        
