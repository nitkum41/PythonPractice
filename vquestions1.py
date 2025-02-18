###1. Write a program to find the second largest number in a list.

def second_largest(numbers):
    unique_numbers = list(set(numbers)) # Remove duplicates
    unique_numbers.sort(reverse=True) # Sort in descending order
    return unique_numbers[1] # Second largest number
numbers = [12, 35, 1, 10, 34, 1]
print(second_largest(numbers)) # Output


##sorted
a=[500,300,400,200,100]
print(a)#[500, 300, 400, 200, 100]
print(sorted(a)) #[100, 200, 300, 400, 500] ##ascending
print(sorted(a , reverse=True))   #descending

##reversed

a =[10,20,30,40,50]
print(a)
b = list(reversed(a))#[10, 20, 30, 40, 50]
print(b) #[50, 40, 30, 20, 10]



## extend and append

a = [1,2,3,4,5]
b = [6,7,8]
a.extend(b)
print(a)#[1, 2, 3, 4, 5, 6, 7, 8]
c = ['a','b']

a.append(c)
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, ['a', 'b']]




###List elements can be turned into a string using join function.

a = [1,2,3,4,5,6,7,8]
print(a)
str1 = (str(i) for i in a)
print(type(str1))  ### generator
numbers = ','.join(str1)
print(numbers)

### randomize list values

from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

