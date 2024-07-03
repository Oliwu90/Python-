def SQL_export_as_csv(what_is_sql_file_name, what_is_sql_file_dir = cwd, save_to_where_default_download_folder = path_to_download_folder):
    def time_convert(sec):
        
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print('\n' + "- Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

   
    ### start stopwatch
    start_time = time.time()
    start_time_now = datetime.datetime.now()

    print("""
--------------------------------------------------
START

- Start time:       {0}
- File_name_read:   {1}
- File_name_where:  {2}
""".format(start_time_now, what_is_sql_file_name,what_is_sql_file_dir)
    )
    try:
        ### connect to sever
        mydb = pymysql.connect(
            database =  'db',
            host =      'host',
            user =      'user',
            password =  'password',
        )
        print("- CONNECTED" )
        
        ### read sql file
        with open(what_is_sql_file_dir + '/' + str(what_is_sql_file_name) + '.sql', 'rb') as f:
            for statement in sqlparse.split(f.read()):
                if not statement:
                    continue
                ### print(statement + '\n')
                print('- Running query.....' )
                cur = mydb.cursor()
                cur.execute(statement)
                rows = cur.fetchall()
            print("- Finished SQL statement")
            # print("--------------------------------------------------")
            # print("              Finished SQL statement   ")
            # print("--------------------------------------------------" + '\n')
        if rows:
            # New empty list called 'result'. This will be written to a file.
            result = list()

            # The row name is the first entry for each entity in the description tuple.
            column_names = list()
            for i in cur.description:
                column_names.append(i[0])

            result.append(column_names)
            for row in rows:
                result.append(row)

            # Write result to file.
            with open(save_to_where_default_download_folder + '/' + str(what_is_sql_file_name) + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in result:
                    csvwriter.writerow(row)
        else:
            column_names = [i[0] for i in cur.description]
            fp = open(save_to_where_default_download_folder + '/' + str(what_is_sql_file_name) + '.csv', 'w', newline='', encoding='utf-8')
            myFile = csv.writer(fp, lineterminator = '\n') #use lineterminator for windows
            myFile.writerow(column_names)
            myFile.writerow(["no data found"])
            myFile.writerow(result)
            fp.close()
            sys.exit("---No data found from query---")

        
        print("- Finished export to csv file")
        print("""- csv file directory: {0}""".format(save_to_where_default_download_folder + '\\' + what_is_sql_file_name + '.csv')
        )
        ### calculating elasped time and end time
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)
        end_time_now = datetime.datetime.now()
        print('- End time {0}'.format(end_time_now))

    except Exception as error:
            print("Exception thrown: {0}".format(error))
    finally:
        mydb.close()
        print('''
CLOSED 
--------------------------------------------------''' + '\n')
