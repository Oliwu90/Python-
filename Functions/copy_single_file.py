def copy_single_file(src_dir, src_dir_file_name_ext, dest_dir, dest_dir_new_file_name_ext):
    # Construct full paths for the source and destination files
    src_file_path = os.path.join(src_dir, src_dir_file_name_ext)
    dest_file_path = os.path.join(dest_dir, dest_dir_new_file_name_ext)

    try:
        # Copy the file from the source to the destination
        shutil.copyfile(src_file_path, dest_file_path)
        print('File copied successfully:')
        print('  Source: ' + src_file_path)
        print('  Destination: ' + dest_file_path)
    except FileNotFoundError:
        print('Error: Source file not found:', src_file_path)
    except PermissionError:
        print('Error: Permission denied. Check permissions for:', dest_dir)
    except shutil.SameFileError:
        print('Error: Source and destination files are the same:', src_file_path)
    except Exception as e:
        print('An error occurred:', e)
