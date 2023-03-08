import os

path = input('Путь: ' )

print("Диреткории:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

print("\nФайлы:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)
