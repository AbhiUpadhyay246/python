import os

# Specify the directory path
directory_path = "/Users"

# List and print directory contents
try:
    for item in os.listdir(directory_path):
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")

