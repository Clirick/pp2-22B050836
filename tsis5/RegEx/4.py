import re

text = input("Enter text: ")

matches = re.findall(r'[A-Z][a-z]+', text)

for match in matches:
    print('sequence:',match)
