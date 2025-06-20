# Downloads File Organizer

A beginner-friendly Python script that organizes files in your **Downloads** folder by automatically moving them into categorized subfolders based on file type (e.g., images, videos, documents, etc.).

## Features

- Automatically organizes your Downloads folder
- Categorizes files by type:
  - **Images** (.jpg, .png, .webp, etc.)
  - **Videos** (.mp4, .mkv, .mov)
  - **Audio** (.mp3, .wav)
  - **Documents** (.pdf, .docx, .txt)
  - **Setup Files** (.exe, .msi)
  - **Packages** (.zip)
- Automatically creates folders if they don’t exist
- Skips directories and unknown file types

## Project Structure

- `downloads_file_organizer.py` – Main script that performs the file categorization and organization

## How to Use

1. Update the `DOWNLOADS_PATH` variable in the script to match your actual Downloads folder path.
2. Run the script using:
   ```bash
   python downloads_file_organizer.py
3. The script will organize your files into folders based on their file extensions.

## Code Design

- Uses `os` and `shutil` for file system operations
- FIle extensions are mapped to categories using a Python dictionary
- The script filters only files (ignores directories) and checks extensions case-insensitively

## Possible Future Improvements
- Add support for uncategorized file types (e.g., move to `others` folder)
- Add a logging system for moved files
- Add undo or backup mechanism
- Make into a GUI or CLI tool for intractive use