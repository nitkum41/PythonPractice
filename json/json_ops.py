# Python program to convert
# Python to JSON


import json

# Data to be written----------------------------------------------------
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json into json string
json_object = json.dumps(dictionary, indent=4)
print(type(json_object),json_object)

# Data to be written--------------------------
dictionary1 = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary1, outfile)


#################loads and load##########

data = {
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}

##file creation and object to file
with open("data_file.json", "w") as write:
    json.dump( data , write )


##reading file into object
with open("data_file.json", "r") as read_content:
    print(json.load(read_content))

# JSON string:
# Multi-line string
data = """{  
    "Name": "Jennifer Smith",  
    "Contact Number": 7867567898,  
    "Email": "jen123@gmail.com",  
    "Hobbies":["Reading", "Sketching", "Horse Riding"]  
    }"""

# parse data to a data type
res = json.loads(data)

# the result is a Python dictionary:
print(res)