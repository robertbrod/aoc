import os

def create_input_dirs(year):
    for i in range(1, 26, 1):
        try:
            path = f"{year}/{i}"
            os.makedirs(path)
        except Exception as error:
            print(f"Skipping directory creation: {path}")
            
def cache_input_data(data, year, day):
    with open(f"{year}/{day}/{year}_{day}_input.txt", "w") as file:
        file.write(data)