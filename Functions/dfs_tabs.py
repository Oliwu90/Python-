def dfs_tabs(df_list, sheet_list, file_name):
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')   
    for dataframe, sheet in zip(df_list, sheet_list):
        if not dataframe.empty:
            dataframe.to_excel(writer, sheet_name=sheet, startrow=0, startcol=0, index=False, header=True)   
    writer.close()
