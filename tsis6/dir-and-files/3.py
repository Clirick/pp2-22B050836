import os

path = input("Путь: ")

if os.path.exists(path):
    file_name = os.path.basename(path)
    directory = os.path.dirname(path)
    
    print("Путь существует")
    print(f"Имя файла: {file_name}")
    print(f"Директория: {directory}")
else:
    print(f"Путь {path} не существует")
