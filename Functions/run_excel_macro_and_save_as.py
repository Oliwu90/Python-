def run_excel_macro_and_save_as (file_path_with_extension , VBA_macro_name, VBA_procedure_name, saved_path):
        """
        Execute an Excel macro
        :param file_path_with_extension : path to the Excel file holding the macro
        :param VBA_macro_name: VBA name
        :param VBA_procedure_name: name in the sub routine
        :param saved_path: path want to be saved as Excel Macro
        :param separator_char: the character used by the operating system to separate pathname components
        :return: None
        """
        xl = win32.Dispatch('Excel.Application')
        # xl = win32.gencache.EnsureDispatch('Excel.Application')
        xl.Application.visible = True
        today = datetime.date.today().strftime('%m-%d-%Y')
        workbook_name = os.path.splitext(os.path.basename(file_path_with_extension ))[0] 
        # os.sep is \
        try:
                print("opening:" + str(file_path_with_extension.split(sep=os.sep)[-1]))
                
                wb = xl.Workbooks.Open(os.path.abspath(file_path_with_extension ))
                print("opened:" + str(file_path_with_extension.split(sep=os.sep)[-1]))

                xl.Application.run("'" + file_path_with_extension.split(sep=os.sep)[-1] + "'" + "!" + VBA_macro_name + "." + VBA_procedure_name)
                print("running VBA...")
                print("finished:" + str(file_path_with_extension.split(sep=os.sep)[-1]))

                wb.Save()
                print("saved:" + str(file_path_with_extension.split(sep=os.sep)[-1]))

                wb.SaveAs(Filename=saved_path + "\\" + workbook_name + today, FileFormat=52)
                print("save as:" + str(file_path_with_extension.split(sep=os.sep)[-1]))

                wb.Close()
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
