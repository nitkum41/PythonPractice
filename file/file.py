# write a file

fo = open("file.txt", 'w+')
for i in range(10):
    fo.write(f"This is the {i}line\n")
fo.close()

# append
fa = open("file.txt", 'a+')
for i in range(10):
    fa.write(f"This is the appended {i}line\n")

fa.close()

# read a file
# fr = open("file.txt", 'r')
with open("file.txt", 'r') as fr:
    if fr.mode == 'r':
        content = fr.readline()  # only first line
        contents = fr.readlines()  # returns list of lines

print(content)
print(contents)
fr.close()
