print("Enter a string to test:")
test_string = input()

new_string = test_string.replace(" ", ":").replace(",", ":").replace(".", ":")

print("The new string is:")
print(new_string)
