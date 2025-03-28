import re



### https://urlregex.com/index.html

str = "please search on this link http://www.google.com"

##### returns list of matched objects in this case urls

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)

print(url)