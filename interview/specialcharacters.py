import  re

str = "Pro1@3ghtyu678& *_?"

regex = re.compile('[!@#$%^&*()_:<>?(){}~\|/]')

if regex.search(str)==None:
    print("no special characters")
else:
    print("string contains special characters")
