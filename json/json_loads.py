import json

with open("dump_data.json","r") as fp:
    #load json data into dictionary if json has data in dic format
    # json_obj = json.load(fp)

    #load json data into json string if json has data in json format
    json_obj = json.load(fp)

# convert json string to string
print(json_obj,type(json_obj))

# convert json string into object type
data = json.loads(json_obj)
#
print(data,type(data))