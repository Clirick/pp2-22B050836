file_path = input("Путь: ")

with open(file_path, 'r') as file:
    line_count = len(file.readlines())

print(f"Количество строк: {line_count}")
