import os

path = input("Путь: ")

if not os.path.exists(path):
    print(f"Путь {path} не существует")
else:
    access = os.access(path, os.R_OK | os.W_OK | os.X_OK)
    if access:
        print(f"{path} доступен для чтения, записи и выполнения")
    else:
        if not os.access(path, os.R_OK):
            print(f"Нет доступа к чтению {path}")
        if not os.access(path, os.W_OK):
            print(f"Нет доступа к записи {path}")
        if not os.access(path, os.X_OK):
            print(f"Нет доступа к выполнению {path}")
