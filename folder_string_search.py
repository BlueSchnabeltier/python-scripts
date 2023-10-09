from os import walk, path
from zipfile import ZipFile, ZIP_DEFLATED

def search_string_in_file(file_path, search_string):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            if search_string in file.read():
                return True

    except Exception as e:
        print(f"Error while processing {file_path}: {e}")

    return False

def collect_files_with_string(folder_path, search_string):
    found_files = []

    for root, _, files in walk(folder_path):
        for file_name in files:
            file_path = path.join(root, file_name)

            if search_string_in_file(file_path, search_string):
                found_files.append(file_path)

    return found_files

def create_zip_from_files(zip_name, file_list):
    with ZipFile(zip_name, "w", ZIP_DEFLATED) as zipf:
        for file_path in file_list:
            arcname = path.relpath(file_path, start=folder_path)

            zipf.write(file_path, arcname)

folder_path = input("Enter folder path: ")
search_string = input("Enter the string to search for: ")
found_files = collect_files_with_string(folder_path, search_string)

if found_files:
    zip_name = f"{folder_path}.zip"

    create_zip_from_files(zip_name, found_files)
    print(f"Zip file \u0022{zip_name}\u0022 created with matching files.")

else:
    print(f"No files containing \u0022{search_string}\u0022 found in the folder.")
