


def reverseNum(num):
    rev=0
    while num!=0:
        rem=num%10
        num=num//10
        print(rem,num)

        rev=rev*10 + rem
        return rev

res=reverseNum(12345)
print(res)