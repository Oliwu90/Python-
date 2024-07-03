def move_files_to_archive(source_folder,archive_folder):
#     source_folder = str(pathlib.Path(__file__).parent.resolve())
    for filename in os.listdir(source_folder):
        if filename.endswith(tuple(['.xlsx', '.csv'])):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(archive_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {archive_folder}")
# Example usage
# archive_path = create_archive_folder()
# move_files_to_archive(archive_path)
