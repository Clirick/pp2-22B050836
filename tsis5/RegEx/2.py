import re

pattern = r'a[bb]{2,3}'

string = input("Enter a string to test: ")

if re.match(pattern, string):
    print(string, 'matches the pattern')
else:
    print(string, 'does not match the pattern')
