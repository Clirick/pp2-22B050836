import string

alphabet = string.ascii_uppercase

for letter in alphabet:
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"This is the file {filename}")

