
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

if __name__ == "__main__":
    # Test it on a specific folder (Be careful! Use a test folder first)
    path_to_clean = input("Enter the full path of the folder you want to clean: ")
    organize_folder(path_to_clean)
