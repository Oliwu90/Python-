def create_folder(download_folder, base_folder_name):
    # Get the list of existing folders
    existing_folders = [folder for folder in os.listdir(download_folder) if os.path.isdir(os.path.join(download_folder, folder))]
    
    # Calculate the next folder number
    next_folder_number = len(existing_folders) + 1
    
    # Generate the folder name using the base folder name and the next folder number
    new_folder_name = f"{base_folder_name}_{next_folder_number}"
    
    # Create the new folder
    new_folder_path = os.path.join(download_folder, new_folder_name)
    os.makedirs(new_folder_path)
    
    return new_folder_path
  
# # Example usage:
# download_folder = user_download_folder_path
# base_folder_name = mf.current_cript_name

# new_folder_path = create_folder(download_folder, base_folder_name)
# print("New folder created:", new_folder_path)
