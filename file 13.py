import os

file_path = os.getcwd()

p = f"{file_path}/simple.txt"
if os.path.isfile(p):
    print("file is exixst")
else:
    print("file not found!")

