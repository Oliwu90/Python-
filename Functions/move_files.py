def move_files_a_list(list_copy_files_name,extension ,from_src,to_des):
    """
    move a list of files to ny its name and its extension
    """
    
    for filename in list_copy_files_name:
        if filename.endswith('.' + extension  ):
            shutil.move( from_src +  '\\' + filename, to_des+"\\")
    print('move files are: ' + filename + '\n')
    print('move files FROM: ' + str(from_src)+ '\n')
    print('move files TO: ' + str(to_des)+ '\n')

def move_files_by_extension(extension ,from_src,to_des):
    """
    move a list of files baed on extension
    """
    ### Search files with .txt extension in source directory
    pattern = r"\*."  + extension 
    
    ### this is a list of dir + file_name + extension
    files = glob.glob(from_src + pattern)
    print('move files FROM: ' + str(from_src))
    print('move files TO: ' + str(to_des))
    
    for file in files:
        ### extract file name form file path
        file_name = os.path.basename(file)
        ### move files from src to des based on file extension
        shutil.move( from_src +  '\\' + file_name, to_des+"\\")
        print('move files is: ' + file_name)
    print('\n')


def move_files_by_filename(pattern,from_src,to_des):
    """
    move a list of files baed on extension
    mf.move_files_by_filename('*New Logic_A Month A head*.xlsx',user_download_folder_path, str(pathlib.Path(__file__).parent.resolve()))
    """
    ### Search files with .txt extension in source directory
    
    ### this is a list of dir + file_name + extension
    files = glob.glob(from_src +'\\' + pattern)
    print('move files FROM: ' + str(from_src))
    print('move files TO: ' + str(to_des))
    
    for file in files:
        ### extract file name form file path
        file_name = os.path.basename(file)
        ### move files from src to des based on file extension
        shutil.move( from_src +  '\\' + file_name, to_des+"\\")
        print('move files is: ' + file_name)
    print('\n')    

def move_files_by_extension_override(extension ,from_src,to_des):
    """
    move a list of files baed on extension
    """
    ### Search files with .txt extension in source directory
    pattern = r"\*."  + extension 
    
    ### this is a list of dir + file_name + extension
    files = glob.glob(from_src + pattern)
    print('move files FROM: ' + str(from_src))
    print('move files TO: ' + str(to_des))
    
    for file in files:
        ### extract file name form file path
        file_name = os.path.basename(file)
        ### move files from src to des based on file extension
        shutil.move( from_src +  '\\' + file_name, to_des+"\\"+ file_name)
        print('move files is: ' + file_name)
    print('\n')    
