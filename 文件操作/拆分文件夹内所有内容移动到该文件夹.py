import os
import shutil
from pathlib import Path

def get_unique_destination(root_dir, filename):
    """Generate a unique filename if there's a conflict."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(root_dir, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

def flatten_folder(root_dir):
    """Move all files from subfolders to the root directory."""
    root_dir = os.path.abspath(root_dir)
    
    # Walk through directory
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip root directory
        if dirpath == root_dir:
            continue
            
        # Process each file in current directory
        for filename in filenames:
            source = os.path.join(dirpath, filename)
            
            # Get unique destination filename
            dest_filename = get_unique_destination(root_dir, filename)
            destination = os.path.join(root_dir, dest_filename)
            
            try:
                # Move file to root directory
                shutil.move(source, destination)
                print(f"Moved: {source} -> {destination}")
            except Exception as e:
                print(f"Error moving {source}: {e}")

if __name__ == "__main__":
    # Specify the folder path you want to flatten
    folder_path = input("输入你的文件夹地址（请直接复制文件夹地址）: ")
    
    if os.path.exists(folder_path):
        flatten_folder(folder_path)
        print("Done!")
    else:
        print("Error: Folder does not exist!")