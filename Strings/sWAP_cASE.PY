s = input()
empty_string =""
for i in s:
    if i.isupper() == True:
        empty_string+= (i.lower())
    else:
        empty_string+= (i.upper())
print(empty_string)
