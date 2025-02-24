### factorial

# num = int(input("enter a number"))
#
# prod=1
# if num ==0:
#     print(prod)
# else:
#     for i in range(1,num+1):
#         prod*=i
#     print(prod)


### method 2 recursion

# def fact(num):
#     if num==0:
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(int(input("enter a number"))))


### ternary operator and recursion

def fact(num):
        return 1 if (num==0) else num*fact(num-1)
print(fact(int(input("enter a number"))))

