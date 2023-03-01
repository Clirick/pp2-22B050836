snake_case_str = input("Enter a snake case string: ")

words = snake_case_str.split('_')

for i in range(1, len(words)):
    words[i] = words[i].capitalize()

camel_case_str = ''.join(words)

print("Camel case string:", camel_case_str)
