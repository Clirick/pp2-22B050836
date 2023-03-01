import re

s = input("Enter a string: ")

result = re.findall('[A-Z][^A-Z]*', s)

print(result)
