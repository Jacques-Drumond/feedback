import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def store_file(folder, file):
    with open(f"{folder}{file.name}.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)