import os

file_path = "tsis6\dir-and-files\del.txt"

if os.path.exists(file_path):

    if os.access(file_path, os.W_OK):

        os.remove(file_path)
        print(f"File {file_path} deleted")

    else:
        print(f"You don't have write access to {file_path}")
else:
    print(f"File {file_path} not exist")
