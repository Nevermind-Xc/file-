import os

def delete_non_achievement_files(root_dir):
    root_dir = os.path.abspath(root_dir)
    print("请输入你要保留的关键词（例如：事迹材料）：")
    a = input()
    keyword = a
    
    # Walk through directory
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check if keyword is not in filename
            if keyword not in filename:
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    # Specify the folder path
    folder_path = input("Enter the folder path to process: ")
    
    if os.path.exists(folder_path):
        confirm = input(" Please confirm (y/n): ")
        if confirm.lower() == 'y':
            delete_non_achievement_files(folder_path)
            print("Done!")
        else:
            print("Operation cancelled.")
    else:
        print("Error: Folder does not exist!")