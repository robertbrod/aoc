import os

def create_input_dirs(year):
    for i in range(1, 26, 1):
        try:
            path = f"{year}/{i}"
            os.makedirs(path)
        except Exception as error:
            print(f"Skipping directory creation: {path}") 