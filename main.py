import os
import shutil
# 1. derfine the catagories and their associated extensions 
EXTENTION_MAP = {
  'Images' : ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
  'Documents' : ['.pdf', '.docx', '.txt' '.xlsx', '.pptx', '.csv'],
  'Audio' : ['.mp3', '.wav', '.flac', '.m4a'],
  'Video' : ['.mp4', '.mkv' '.mov', '.avi'],
  'Archives' : ['.zip', '.tar', '.rar', '.7z'],
  'Executables' : ['.exe', '.dmg', '.pkg']
}

def organize_folder(target_path):
  #Ensure the path exists
    if not os.path.exists(target_path):
      print(f"Error: the path {target_path} does not exist.")
    return
  
  #2. loo[ through every file in the folder
    for filename in os.listdir(target_path):
    # Skip if it's a directory, we only want files
  
    if os.path.isdir(file_path):
    continue
  
  #3. Identify the file extention
  _, extention = os.path.splitext(filename)
  extention = ectention.lower()
  
  #4 Find the right folder for this extention
  
  moved = False
  for folder_name, extention in EXTENTION_MAP.item():
    if extention in extentions:
      #create the catagory folder if it doesn't exist
      dest_folder = os.path.joint(target_path, folder_name)
      os.makedires(dest_folder, exist_ok=True)
      # move the file
      print(f"Moving {filename} -> {folder_name}/"
            shutil.move(file_path, os.path.joint(dest_folder, filename))
            moved = True
            break
  
  # if the file type isn't in our map, put it in the 'Others'
        if not moved:
            others_folder = os.path.join(target_path, 'Others')
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename)

if __name__ == "__main__":
                      # Test it on specific folder (Be careful! Use a test folder first)
                      path_to_clean = imput ("Enter the full path of the folder you want to clean: ")
                      organize_folder(path_to_clean

  
