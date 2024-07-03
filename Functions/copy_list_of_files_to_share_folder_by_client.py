def copy_list_of_files_to_share_folder_by_client(list_copy_files_name,extension ,from_src,created_folder_name,created_root_path):
    """
    copy a list of files to assigned sharefolder
    """
    ### declare variables
    dir_download = str(os.path.join(Path.home(), "Downloads"))
    dir_month = datetime.datetime.now().strftime('%Y.%m')
    dir_today = datetime.datetime.now().strftime('%m.%d')
    check_dir_1 = created_root_path + '\\' + created_folder_name
    check_dir_2 = check_dir_1 + '\\' + dir_month
    check_dir_3 = check_dir_2 + '\\' + dir_today

    ### part 1 
    ### check if diretory exist
    ### if not, create it 
    print('checking if directory exist: ' + check_dir_1)
    print(str(os.path.exists(check_dir_1)) + '\n')
    if not os.path.exists(check_dir_1):
        os.makedirs(check_dir_1)
        print('created dir: ' + check_dir_1 + '\n')

    ### part 2
    ### check if diretory exist
    ### if not, create it
    print('checking if directory exist: ' + check_dir_2)
    print(str(os.path.exists(check_dir_2))+ '\n')
    if not os.path.exists(check_dir_2):
        os.makedirs(check_dir_2)
        print('created dir: ' + check_dir_2)
    
    ### part 3
    ### check if diretory exist
    ### if not, create it
    print('checking if directory exist: ' + check_dir_3)
    print(str(os.path.exists(check_dir_3))+ '\n')
    if not os.path.exists(check_dir_3):
        os.makedirs(check_dir_3)
        print('created dir: ' + check_dir_3)
    
    for filename in list_copy_files_name:
        if filename.endswith('.' + extension  ):
            shutil.copy( from_src + filename, check_dir_3+"\\")
    print('move files are: ' + filename + '\n')
    print('move files FROM: ' + str(from_src)+ '\n')
    print('move files TO: ' + str(check_dir_3)+ '\n')
