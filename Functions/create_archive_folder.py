def create_archive_folder(source_folder):
    
    # Create the archive folder if it doesn't exist
    # source_folder = str(pathlib.Path(__file__).parent.resolve())

    archive_folder = os.path.join(source_folder, 'Archive')
    os.makedirs(archive_folder, exist_ok=True)

    # Create a subfolder with the year
    year_folder = os.path.join(archive_folder, str(datetime.datetime.now().year))
    os.makedirs(year_folder, exist_ok=True)

    # Create a subfolder with today's date (MMDDYYYY)
    today_date = datetime.datetime.now().strftime('%m%d%Y')
    today_folder = os.path.join(year_folder, today_date)
    os.makedirs(today_folder, exist_ok=True)
    print(today_folder)
    print(f"Created folder ---> {today_folder}")
    return today_folder
