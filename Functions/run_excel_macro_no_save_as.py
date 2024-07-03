def run_excel_macro_no_save_as (file_path_with_extension , VBA_macro_name, VBA_procedure_name):

        """
        Execute an Excel macro
        :param file_path_with_extension : path to the Excel file holding the macro
        :param VBA_macro_name: VBA name
        :param VBA_procedure_name: name in the sub routine
        :param separator_char: the character used by the operating system to separate pathname components
        :return: None
        """
        xl = win32.Dispatch('Excel.Application')
        xl.Application.visible = True
        today = datetime.date.today().strftime('%m-%d-%Y')
        workbook_name = os.path.splitext(os.path.basename(file_path_with_extension ))[0] 
        # os.sep is \
        try:
                print("opening:" + str(file_path_with_extension.split(sep=os.sep)[-1]))
                
                wb = xl.Workbooks.Open(os.path.abspath(file_path_with_extension ))
                time.sleep(5)
                print("opened:" + str(file_path_with_extension.split(sep=os.sep)[-1]))
                
                xl.Application.run("'" + file_path_with_extension.split(sep=os.sep)[-1] + "'" + "!" + VBA_macro_name + "." + VBA_procedure_name)
                time.sleep(5)
                print("running VBA...")
                print("finised:" + str(file_path_with_extension.split(sep=os.sep)[-1]))
                
                wb.Save()
                time.sleep(5)
                print("saving:" + str(file_path_with_extension.split(sep=os.sep)[-1]))
                
                wb.Close()
                time.sleep(5)
                print("closed:" + str(file_path_with_extension.split(sep=os.sep)[-1]))
                print("Completed: " + str(file_path_with_extension.split(sep=os.sep)[-1]) + '\n')

                ### add two lines below becasue application doesn't close
                xl.Application.Quit()
                del xl
        except Exception as ex:
                template = "An exception of type {0} occurred. \nArguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)

                xl.Application.Quit()
                del xl
