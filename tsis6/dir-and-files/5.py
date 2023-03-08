my_list = ["1", "word", "orange", "_____"]

with open("my_file.txt", "w") as file:
    for item in my_list:
        file.write(f"{item}\n")
