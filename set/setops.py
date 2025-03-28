a = set([111,21,53,41])

b= set({'a':12,'b':2})

c= {1,2,3,4}

print(type(a))
print(type(b))

print(type(c))

a.add("A")

print(a)


fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

print('Unique elements:', fruits)

# Add new fruit
fruits.add("Orange")
print('After adding new element:', fruits)

# Size of the set
print('Size of the set:', len(fruits))

# check if the element is present in the set
print('Apple is present in the set:', "Apple" in fruits)
print('Mango is present in the set:', "Mango" in fruits)

# Remove the element from the set
fruits.remove("Mango")
print('After removing element:', fruits)

# Discard the element from the set
fruits.discard("Mango")
print('After discarding element:', fruits)