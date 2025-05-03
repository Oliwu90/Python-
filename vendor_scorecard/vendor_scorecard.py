import os
import sys
import time
import traceback
import datetime
import pathlib
from pathlib import Path
from datetime import timedelta
from io import StringIO
from dotenv import load_dotenv
load_dotenv()

import numpy as np
import pandas as pd
import pymysql
import openpyxl
from openpyxl.styles import Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows
import sqlparse 

import mf
import SQL_my_functions
from Credential import MS_app_password_to_send_email

folder_name = mf.create_multiple_folders_by_time()
today = datetime.date.today().strftime('%m%d%y')
current_script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
start = mf.start_time_now()

# Create folder based on current time
folder_name = mf.create_multiple_folders_by_time()
today = datetime.date.today().strftime('%m%d%y')
current_script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
start = mf.start_time_now()

def write_summaries_to_excel(writer, client, *args):
    """
    Write multiple summary dataframes to an Excel sheet for a given client.

    Parameters:
    - writer: pd.ExcelWriter object to write to.
    - client: String name of the client's sheet.
    - *args: Tuples containing ('header_name', dataframe) to be written to the sheet.
    """
    
    # Check if the sheet already exists
    if client in writer.sheets:
        worksheet = writer.sheets[client]
        current_row = worksheet.dim_rowmax + 5  # Continue from the last written row
    else:
        # Create a new sheet for the client
        writer.book.add_worksheet(client)
        worksheet = writer.sheets[client]
        current_row = 0
        
        # Hide gridlines and set the header format
        worksheet.hide_gridlines(option=2)
        header_format = writer.book.add_format({'bold': True, 'font_size': 18})
    header_format = writer.book.add_format({'bold': True, 'font_size': 18})
    # Helper function to write a DataFrame with a header
    def write_summary(worksheet, header, df, start_row):
        worksheet.write(start_row, 0, header, header_format)
        start_row += 1
        df.to_excel(writer, sheet_name=client, startrow=start_row, index=True, header=True)
        return start_row + len(df) + 5

    # Loop over the tuples and write each dataframe with its corresponding header
    for header, df in args:
        current_row = write_summary(worksheet, header, df, current_row)
        
def fetch_data_from_database(sql_query, retries=3, delay=5):
    for attempt in range(retries):
        try:
            mydb = pymysql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("USER_NAME"),
                password=os.getenv("PASSWORD"),
                database=os.getenv("DATABASE"),
                connect_timeout=600,
                read_timeout=600,
                write_timeout=600
            )
            with mydb.cursor() as cursor:
                cursor.execute(sql_query)
                columns = [desc[0] for desc in cursor.description]
                myresult = cursor.fetchall()
                return pd.DataFrame(myresult, columns=columns)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    return None

sql_query = """QUERY GOES HERE"""
df = fetch_data_from_database(sql_query)
df.to_excel(str(pathlib.Path(__file__).parent.resolve()) + '\\' +'1.xlsx', index=False)

# Logicas
df['completeddate'] = pd.to_datetime(df['completeddate'], errors='coerce')
df['completed_mon'] =  df['completeddate'].dt.month

df2 = df.groupby([ 'completed_mon'], as_index=False).aggregate(
                                                                TOTAL_COUNT_APPROVED=('ontime_late', lambda s: s.isin(['OnTime', 'Late']).sum()),
                                                                COUNT_ONTIME =('ontime_late', lambda s: s.eq('OnTime').sum()),
                                                                COUNT_LATE =('ontime_late', lambda s: s.eq('Late').sum()))
df2['ON_TIME_%_APPROVED'] = (df2['COUNT_ONTIME'] / df2['TOTAL_COUNT_APPROVED'] * 100).round(2)

### pivot
pivot_df = df2.pivot_table( columns='completed_mon', values=['TOTAL_COUNT_APPROVED', 'COUNT_LATE', 'ON_TIME_%_APPROVED'], aggfunc='sum',margins=False)

### groupby
df_sum_vendor = df.groupby(['vendorname'], as_index=True).aggregate(
                    Total=('workordernumber', 'count'),
                    Numbers_Of_OnTime =('ontime_late', lambda s: s.eq('OnTime').sum()),
                    Numbers_Of_Late =('ontime_late', lambda s: s.eq('Late').sum()))
df_sum_vendor = df_sum_vendor[df_sum_vendor['Total'] >=50] # note 1
df_sum_vendor['On_Time_%'] = (df_sum_vendor['Numbers_Of_OnTime'] / df_sum_vendor['Total'] * 100).round(2)
df_sum_vendor['Ranks'] = df_sum_vendor['On_Time_%'].rank(ascending=False, method='dense').astype(int)

df.to_excel(str(pathlib.Path(__file__).parent.resolve()) + '\\' +'2.xlsx')

with pd.ExcelWriter(str(pathlib.Path(__file__).parent.resolve()) + '\\'  + f'{current_script_name}{today}.xlsx') as writer:
    write_summaries_to_excel(writer, "Summary", 
                        ('Approved Summary', pivot_df),
                        ("vendor", df_sum_vendor),
                        ("Data",df),
                        )