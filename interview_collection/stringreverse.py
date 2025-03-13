

def reverseString(str1):

    output=""
    for char in str1:
        output = char+output
        print(output)
    return output


str1="Apple"

res=reverseString(str1)

print(res)