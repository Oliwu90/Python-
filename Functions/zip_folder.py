def zip_folder(folder_path):
    # Get the current date
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')

    # Create a zip file name with the directory structure
    zip_file_name = f"{year}/{month}/{day}.zip"

    # Create the directories if they don't exist
    os.makedirs(os.path.dirname(zip_file_name), exist_ok=True)

    # Open a new zip file
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        # Iterate over the files in the folder
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip file
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

    print(f"Folder '{folder_path}' zipped as '{zip_file_name}'")

    # Delete all folders within folder_path
    for folder in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder)
        if os.path.isdir(folder_full_path):
            shutil.rmtree(folder_full_path)

    print(f"All folders within '{folder_path}' deleted.")
# # Specify the folder path to zip
# folder_path = r'C:\Users\Administrator\Downloads'
# # Zip the folder
# zip_folder(folder_path)
