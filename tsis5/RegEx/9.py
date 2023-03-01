import re

s = input("Enter a string: ")

result = re.sub(r'(?<=\w)([A-Z])', r' \1', s)

print(result)
