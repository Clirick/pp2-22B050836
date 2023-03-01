import re

pattern = r'[a-z]+_[a-z]+'

print("Enter a string to test:")
test_string = input()

matches = re.findall(pattern, test_string)

if matches:
    print("match the pattern")
else:
    print("does not match the pattern")
 