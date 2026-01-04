
import os
import shutil

# 1. Define the categories and their associated extensions
EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi'],
    'Archives': ['.zip', '.tar', '.rar', '.7z'],
    'Executables': ['.exe', '.dmg', '.pkg']
}

def organize_folder(target_path):
    # Ensure the path exists
    if not os.path.exists(target_path):
        print(f"Error: The path {target_path} does not exist.")
        return

    # 2. Loop through every file in the folder
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)

        # Skip if it's a directory, we only want files
        if os.path.isdir(file_path):
            continue

        # 3. Identify the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # 4. Find the right folder for this extension
        moved = False
        for folder_name, extensions in EXTENSION_MAP.items():
            if extension in extensions:
                # Create the category folder if it doesn't exist
                dest_folder = os.path.join(target_path, folder_name)
                os.makedirs(dest_folder, exist_ok=True)

                # Move the file
                print(f"Moving {filename} -> {folder_name}/")
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break
        
        # If the file type isn't in our map, put it in 'Others'
        if not moved:
            others_folder = os.path.join(target_path, 'Others')
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            
import tkinter as tk
from tkinter import filedialog
import os

if __name__ == "__main__":
    # 1. Create a hidden background window (so it doesn't look messy)
    root = tk.Tk()
    root.withdraw()

    # 2. Open the Mac folder selection dialog
    print("Please select the folder you want to organize...")
    selected_path = filedialog.askdirectory(title="Select Folder to Organize")

    # 3. Check if the user actually picked a folder or just hit 'Cancel'
    if selected_path:
        organize_folder(selected_path)
        print(f"Success! Folder organized: {selected_path}")
    else:
        print("No folder selected. Exiting.")
