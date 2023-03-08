import shutil

source_file = "C:/Users/oneta/pp2/pp2-22B050836/tsis6/dir-and-files/source.txt"

copy_file = "C:/Users/oneta/pp2/pp2-22B050836/tsis6/dir-and-files/copy.txt"

try:
    shutil.copyfile(source_file, copy_file)
    print(f"Contents of {source_file} copied to {copy_file} successfully!")
except FileNotFoundError:
    print(f"{source_file} not found!")
