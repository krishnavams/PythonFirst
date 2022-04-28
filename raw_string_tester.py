string = "ABcdefgHIjklMnoPQRStuVWxYZ"
print(string.lower(),'lower case')
print(string.upper(),'upper case')
print(string.swapcase(),'swaping cases')
print(string.count("j"),'counting j')
print(string.count('j',-10,-1),'counting j in range')
print(string.find('j',-10,-1),'finding j in range')
print(string.find('ja',-10,-1),'finding ja in range')
print(string.rfind('j',-26,-1),'finding j in revrse') #no of occrences of j in the range
print(string.index("j"),'finding index number')
print(string.rindex("j"),'finding index number in reverse')
print(string.replace('j','z'),'replacing the charactors values')
print(string.startswith('A'),'checking is this start with A or not')
print(string.endswith('Z'),'checking is this Ends with Z or not')
print(string.split('S'),'Spliting with S and it gives list')
string_2 = "    abc    "
print(string.join(string.split('S')),'Joining list')
string_2 = "    abc    "
print(string_2.strip(),'removing spaces')
print(string_2.rstrip(' '),"removing ' ' @ last")
print(string_2.lstrip(' '),"removing ' ' @ ")

