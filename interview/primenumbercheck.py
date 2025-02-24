###check a number is prime or not
import math

###method 1

num = int(input("Enter a number"))

if num <1:
    print("Not prime")
else:
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0:
            print("Not Prime")
            break
    else:
        print("Prime")

###mrthod 2------1 and number itself are the factors
count=0
num = int(input("enter a number"))

if num>1:
    for i in range(1,num+1):
        if num%i == 0:
            count+=1

    if count==2:
        print("prime")
    else:
        print("not prime")
