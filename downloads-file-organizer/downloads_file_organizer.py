# Downloads File Organizer
# Created by Marc Neil Tagle, June 2025
# For educational purposes

import os
import shutil

# update this path to match actual Downloads folder path
DOWNLOADS_PATH = r'C:\Users\User\Downloads'

# defines file type categories and their associated extensions
FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.bmp', '.webp'],
    'videos': ['.mp4', '.mov', '.mkv'],
    'audio': ['.mp3', '.wav'],
    'documents': ['.docx', '.pdf', '.txt'],
    'packages': ['.zip'],
    'setup files': ['.exe', '.msi']
}

def main():

    # lists all items (files and folders) in the Downloads directory
    downloads_files = os.listdir(DOWNLOADS_PATH)

    # create necessary folders for each file type if they don't exist
    for key, value in FILE_TYPES.items():
        dir_path = os.path.join(DOWNLOADS_PATH, key)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Directory created: {dir_path}")

    # go through each item in the Downloads folder
    for file in downloads_files:
        file_path = os.path.join(DOWNLOADS_PATH, file)

        # skips if item is not a file
        if not os.path.isfile(file_path):
            continue 
        
        # separate the file name and extension
        name, extension = os.path.splitext(file)

        # check which category or directory the file belongs to
        for key, value in FILE_TYPES.items():
            # checks if file extension is in file type list
            if extension.lower() in value:
                # move the file to the matching folder
                dir_path = os.path.join(DOWNLOADS_PATH, key)
                shutil.move(file_path, dir_path)
                print(f"File {file} moved successfully to {key}")
                break

if __name__ == '__main__':
    main()