import re

string = input()

matches = re.findall(r'a.*b', string)

for match in matches:
    print("Найденные совпадения:",match)
