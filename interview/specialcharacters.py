import  re

str = "Pro1@3ghtyu678& *_?"
str1="abcde223"

regex = re.compile('[!@#$%^&*()_:<>?(){}~\\|/]')

if regex.search(str)==None:
    print("no special characters")
else:
    print(regex.search(str))
    print("string contains special characters")
