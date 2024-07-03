def create_multiple_folders_by_time():  
        today = datetime.date.today().strftime('%m%d%y')
        t = time.localtime()
        current_time = time.strftime("%H-%M-%S", t)
        des_folder = current_cript_name  + today + '_' + current_time
        user_download_folder_path = os.path.join(Path.home(),"Downloads")
        print(user_download_folder_path + '//' + des_folder)
        create_folder(user_download_folder_path,des_folder)
        save_to_dir = user_download_folder_path + '\\' + des_folder
        return save_to_dir
