mystr="abcaabcdc"

def get_largest_substring(mystr):
    low=0
    up=1
    used={mystr[0]}
    maxbounds=(0,1)

    while up < len(mystr):
        if mystr[up] in used:
            used.remove(mystr[low])
            low+=1
        else:
            used.add(mystr[up])
            up+=1
        if up-low > maxbounds[1]-maxbounds[0]:
            maxbounds=(low,up)

    return mystr[maxbounds[0]:maxbounds[1]]

print(get_largest_substring(mystr))