import json

data = {
    "name":"Nitesh",
    "age":34,
    "roles":["SDET","QA","Tester"]
}

list_data = ["A","B","C"]

print(type(list_data))
#convert dic to string
dump_obj=json.dumps(list_data)

print(dump_obj,type(dump_obj))

with open("dump_data.json", "w") as fp:
    #write json string into file asjson string
    json.dump(dump_obj,fp)
    #
    # fp.write(dump_obj)
    # # #write dictionary into file as dictionary
    # json.dump(list_data,fp)



# print(dump_obj,type(dump_obj))