import re

string = input("Enter a string: ")
pattern = r"a*b*"

match = re.match(pattern, string)

if match:
    print("String matches pattern!")
else:
    print("String does not match pattern.")
