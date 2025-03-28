import re

my_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')

"""
Methods can also be used directly on the re module. 
It does not make that much of a difference, but some people prefer explicitely precompiling and binding the pattern to a reusable variable
"""


### finditer()
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print("finditer",match.group()) # returns the string



# findall()
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print("findall",match)

# search
pattern=re.compile(r'abc')
match3 = pattern.search(my_string)
print("search",match3 , match3.group())

# match
pattern = re.compile(r'123')
match2 = pattern.match(my_string)
print("match",match2 , match2.group())


# pattern = re.compile(r'abc')
# match1 = pattern.match(my_string)
# print(match1)