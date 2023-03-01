def camel_to_snake(s):
    s = ''.join(['_'+i.lower() if i.isupper() else i for i in s])
    if s[0] == '_':
        s = s[1:]
    return s

s = input()
print(camel_to_snake(s)) 
